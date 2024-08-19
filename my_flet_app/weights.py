import random
from constants import *
import flet as ft
import time
import threading

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
    # Порог для определения, что весы пусты (например, вес меньше 1 грамма)
    empty_threshold = 3

    # Диапазоны весов для различных состояний
    states = {
        "empty":(
            -empty_threshold,
            empty_threshold
        ),
        "teapot": (
            empty_teapot_weight - tolerance,
            empty_teapot_weight + tolerance
        ),
        "teapot+leaves": (
            empty_teapot_weight + leaves_min_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + tolerance
        ),
        "teapot+leaves+cap": (
            empty_teapot_weight + leaves_min_weight + cap_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + cap_weight + tolerance
        ),
        "teapot+leaves+water": (
            empty_teapot_weight + leaves_min_weight + water_min_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + water_max_weight + tolerance
        ),
        "teapot+leaves+water+cap": (
            empty_teapot_weight + leaves_min_weight + water_min_weight + cap_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + water_max_weight + cap_weight + tolerance
        ),
        "teapot+leaves+water+cap+unknown": (
            empty_teapot_weight + leaves_max_weight + water_max_weight + cap_weight + tolerance,
            300
        ),
    }

    for state, (min_weight, max_weight) in states.items():
        if min_weight <= weight <= max_weight:
            state_sets = set(state.split('+'))
            return state_sets

    return "not_teapot"


def start(page, progress_ring, remaining_time_text, full_time_text):
    total_steps = total_time * 100
    step_duration = 1 / 100

    for step in range(total_steps, 0, -1):
        time.sleep(step_duration)
        progress_value = step / total_steps

        progress_ring.value = 1.0 - progress_value
        remaining_time = int(step * step_duration)
        remaining_time_text.value = f"{remaining_time} s left"

        page.update()
