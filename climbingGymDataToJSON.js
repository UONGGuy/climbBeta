// ---------------------------------------------------------------
// climbBeta — Google Sheet -> JSON
//
// Sheet layout:
//   Row 1 = title / notes (ignored)
//   Row 2 = headers (cleaned to camelCase as JSON keys)
//   Row 3+ = one gym per row
//
// Key points:
//   - Headers are camelCased in the output. Renaming a sheet header
//     changes the JSON key -> frontend check required.
//   - "id" auto-derived from "Name" if blank.
//   - "last_verified" becomes "lastVerified" (ISO date string).
//   - Website is a label, not a URL (URLs come later via Website URL).
//   - Columns in NO_DROPDOWN_COLUMNS never appear in _dropdown_options,
//     even if a data validation exists on them (guards against stray
//     validations after inserting columns).
// ---------------------------------------------------------------

var SHEET_ID   = '1KURyScK0Utl5HhBn4eEIy6vRx6iU4DlmGz4uYu_jkwI';
var SHEET_NAME = 'ClimbingGyms';
var FOLDER_ID  = '16QceLy56-iBR0wZ9ExMpNGewsUpqJC_w';

// Columns that should never carry a dropdown, regardless of sheet state.
var NO_DROPDOWN_COLUMNS = [
  'id', 'name', 'lastVerified', 'location', 'transport',
  'openingHours', 'website', 'waiver', 'size', 'changingRooms'
];

// ---------- helpers ----------

function toCamelCase(header) {
  var s = String(header).trim();
  s = s.replace(/\([^)]*\)/g, '').trim();          // drop parentheticals
  var parts = s.split(/[^a-zA-Z0-9]+/).filter(Boolean);
  if (parts.length === 0) return '';
  return parts[0].toLowerCase() +
    parts.slice(1).map(function (p) {
      return p.charAt(0).toUpperCase() + p.slice(1).toLowerCase();
    }).join('');
}

function slugify(name) {
  return String(name)
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

// Strip a single pair of surrounding double quotes and trim whitespace.
function cleanCell(value) {
  if (typeof value !== 'string') return value;
  var s = value.trim();
  if (s.length >= 2 && s.charAt(0) === '"' && s.charAt(s.length - 1) === '"') {
    s = s.substring(1, s.length - 1).trim();
  }
  return s;
}

// ---------- shared: build JSON from sheet ----------

function buildData() {
  var sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName(SHEET_NAME);
  if (!sheet) throw new Error('Sheet "' + SHEET_NAME + '" not found.');

  var values = sheet.getDataRange().getValues();
  if (values.length < 3) throw new Error('Sheet has no data rows.');

  var rawHeaders = values[1];                       // row 2

  // build header -> camelKey map
  var keysByIndex = [];
  var headerMap = {};
  for (var j = 0; j < rawHeaders.length; j++) {
    var key = toCamelCase(rawHeaders[j]);
    keysByIndex[j] = key;
    if (rawHeaders[j]) headerMap[String(rawHeaders[j]).trim()] = key;
  }

  // ---------- rows ----------
  var jsonData = [];
  for (var i = 2; i < values.length; i++) {
    var row = values[i];
    if (!row[0]) continue;                          // skip empty rows

    var obj = {};
    for (var j = 0; j < keysByIndex.length; j++) {
      if (!keysByIndex[j]) continue;
      obj[keysByIndex[j]] = cleanCell(row[j]);
    }

    // id: use sheet value if present, else derive from name
    if (!obj.id && obj.name) obj.id = slugify(obj.name);

    jsonData.push(obj);
  }

  // ---------- dropdowns ----------
  var dropdowns = {};
  for (var c = 0; c < rawHeaders.length; c++) {
    var key = keysByIndex[c];
    if (!key) continue;
    if (NO_DROPDOWN_COLUMNS.indexOf(key) !== -1) continue;

    var validation = sheet
      .getRange(3, c + 1, sheet.getLastRow() - 2)
      .getDataValidations();
    var options = new Set();

    for (var k = 0; k < validation.length; k++) {
      for (var l = 0; l < validation[k].length; l++) {
        var rule = validation[k][l];
        if (rule && rule.getCriteriaType() === SpreadsheetApp.DataValidationCriteria.VALUE_IN_LIST) {
          var args = rule.getCriteriaValues();
          args[0].forEach(function (o) { options.add(o); });
        }
      }
    }
    if (options.size > 0) dropdowns[key] = Array.from(options);
  }

  return {
    data: jsonData,
    _header_map: headerMap,
    _dropdown_options: dropdowns
  };
}

// ---------- web app endpoint ----------

function doGet() {
  try {
    return ContentService
      .createTextOutput(JSON.stringify(buildData()))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// ---------- optional Drive snapshot (currently unused) ----------

function exportSheetToJSON() {
  try {
    var jsonOutput = JSON.stringify(buildData(), null, 2);
    var folder = DriveApp.getFolderById(FOLDER_ID);
    var file = folder.createFile('ClimbingGymsData.json', jsonOutput, 'application/json');
    Logger.log('JSON file created: ' + file.getUrl());
  } catch (err) {
    Logger.log('Export failed: ' + err);
  }
}