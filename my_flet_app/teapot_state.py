from enum import Enum, auto

class TeapotStatus(Enum):
    EMPTY = auto()
    TEAPOT = auto()
    TEAPOT_LEAVES = auto()
    TEAPOT_LEAVES_CAP = auto()
    TEAPOT_LEAVES_WATER = auto()
    TEAPOT_LEAVES_WATER_CAP = auto()
    TEAPOT_UNKNOWN = auto()
    NOT_TEAPOT = auto()

class TeapotState:
    def __init__(self, count: int, full_time: int, current_time: int, iteration_time: int, teapot_status: TeapotStatus):
        self.count = count
        self.full_time = full_time
        self.current_time = current_time
        self.iteration_time = iteration_time
        self.teapot_status = teapot_status
