from dataclasses import dataclass
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


@dataclass
class TeapotState:
    def __init__(self, count: int, full_time: int, current_time: int, iteration_time: int, teapot_status: TeapotStatus,
                 cup: int, leaf: int, water: int, lid: int, is_time_alarm: bool):
        self.count = count
        self.full_time = full_time
        self.current_time = current_time
        self.iteration_time = iteration_time
        self.teapot_status = teapot_status
        self.cup = cup
        self.leaf = leaf
        self.water = water
        self.lid = lid
        self.is_time_alarm = is_time_alarm

    def __eq__(self, other):
        # Compare only the fields that matter
        return (
            self.count, self.current_time, self.full_time, self.iteration_time, self.teapot_status, self.lid, self.cup,
            self.leaf, self.water, self.is_time_alarm) == (
            other.count, other.current_time, other.full_time, other.iteration_time, other.teapot_status, other.lid,
            other.cup, other.leaf, other.water, other.is_time_alarm)
