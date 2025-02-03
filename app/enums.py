# enums.py
# Contain enumerated types to be used with models.py in defining shared features across climbing gyms.

from enum import Enum, auto

class BaseEnum(Enum):
    # Base class to build all other enums which require simple custom string representation
    def __str__(self):
        # Return custom string representation
        # TEST_ENUM.name --> Test Enum
        return self.name.replace("_", " ").title()


class eFranchiser(BaseEnum):
    # Store climbing gym franchisers
    CITY_BOULDERING = auto()
    LONDON_CLIMBING_CENTER = auto()
    CASTLE_CLIMBING = auto()
    YONDER_CLIMBING = auto()
    RISE_CLIMBING = auto()
    ARCH_CLIMBING = auto()
    PARTHIAN_CLIMBING = auto()
    MILE_END_CLIMBING = auto()
    STRONGHOLD_CLIMBING_CENTERS = auto()
    THE_FONT = auto()
    HANG_ABOUT_LTD = auto()


class eClimbActivities(BaseEnum):
    # Store climbing activities
    BOULDERING = auto()
    LEAD_CLIMBING = auto()
    TOP_ROPE = auto()
    AUTO_BELAYS = auto()

class eLockerTypes(BaseEnum):
    # Store locker types
    COIN = auto()
    PADLOCK = auto()

class eClimbTrainEquipment(BaseEnum):
    # Store climbing training equipment
    FINGERBOARD = auto()
    HANGBOARD = FINGERBOARD
    CAMPUS_BOARD = auto()
    PINCH_BLOCK = auto()
    LIFTING_EDGE = auto()

class eClimbBoard(BaseEnum):
    # Store climbing board types
    # Additional details on boards to be implemented in models.py
    KILTER_BOARD = auto()
    MOONBAORD = auto()
    TENSION_BOARD = auto()


