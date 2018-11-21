from enum import Enum


class PyAxisMap(Enum):
    # Access as integers by using PyAxisMap.NAME_HERE.value
    LEFT_THUMB_X = 0        # +ve direction is right
    LEFT_THUMB_Y = 1        # +ve direction is down
    RIGHT_THUMB_X = 2       # +ve direction is right
    RIGHT_THUMB_Y = 3       # +ve direction is down
    RIGHT_TRIGGER = 4       # +ve direction is pushed in
    LEFT_TRIGGER = 5        # +ve direction is pushed in


class PyButtonMap(Enum):
    # Access as integers by using PyAxisMap.NAME_HERE.value
    A = 0
    B = 1
    X = 2
    Y = 3
    LEFT_BUTTON = 4
    RIGHT_BUTTON = 5
    BACK = 6
    START = 7
    XBOX_HOME = 8
    LEFT_THUMB_IN = 9
    RIGHT_THUMB_IN = 10


class PyHatMap(Enum):
    # NOTE for DPAD (it's a hat) you get ONE hat, which is a tuple of
    # (horizontal [-1 = left or 0 or 1 = right], vertical [-1 = down or 0 or 1 = up])
    # Access as integers by using PyAxisMap.NAME_HERE.value
    DPAD = 0
