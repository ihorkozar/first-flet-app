import random
import threading
import time

from bloc.teapot_state import TeapotStatus
from utils.app_constants import *


def noise(level=tolerance):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            noise_value = (random.random() * level / 200) * random.choice([-1, 1])
            return result + noise_value

        return wrapper

    return decorator


@noise(level=empty_threshold)
def empty():
    return 0


@noise()
def empty_teapot():
    return empty() + empty_teapot_weight + leaves_min_weight


@noise()
def full_teapot():
    return empty_teapot() + water_max_weight + cap_weight


@noise()
def full_teapot_cap():
    return empty_teapot() + leaves_max_weight + water_max_weight + cap_weight + tolerance


def identify_teapot_state(weight):
    empty_threshold = 3

    states = {
        TeapotStatus.EMPTY: (
            -empty_threshold,
            empty_threshold
        ),
        TeapotStatus.TEAPOT: (
            empty_teapot_weight - tolerance,
            empty_teapot_weight + tolerance
        ),
        TeapotStatus.TEAPOT_LEAVES: (
            empty_teapot_weight + leaves_min_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + tolerance
        ),
        TeapotStatus.TEAPOT_LEAVES_CAP: (
            empty_teapot_weight + leaves_min_weight + cap_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + cap_weight + tolerance
        ),
        TeapotStatus.TEAPOT_LEAVES_WATER: (
            empty_teapot_weight + leaves_min_weight + water_min_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + water_max_weight + tolerance
        ),
        TeapotStatus.TEAPOT_LEAVES_WATER_CAP: (
            empty_teapot_weight + leaves_min_weight + water_min_weight + cap_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + water_max_weight + cap_weight + tolerance
        ),
        TeapotStatus.TEAPOT_UNKNOWN: (
            empty_teapot_weight + leaves_max_weight + water_max_weight + cap_weight + tolerance,
            300
        ),
    }

    for state, (min_weight, max_weight) in states.items():
        if min_weight <= weight <= max_weight:
            return state

    return TeapotStatus.NOT_TEAPOT


def numbers_stream(observer, scheduler):
    def emit():
        observer.on_next(0.)
        values = [
            (empty, 2),
            (empty_teapot, 1),
            (full_teapot, 3),
            (full_teapot_cap, 3),
            (empty_teapot, 2),
            (full_teapot, 18),
            (empty, 4),
        ]
        delay = 0.1

        for func, count in values:
            for _ in range(int(count / delay)):
                observer.on_next(func())
                time.sleep(delay)

        observer.on_completed()

    threading.Thread(target=emit).start()
