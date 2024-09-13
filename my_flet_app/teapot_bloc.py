import random
from threading import Timer
from typing import Callable, List

from app_constants import *
from teaport_event import *
from teapot_state import TeapotStatus, TeapotState


class TeapotBloc:
    def __init__(self):
        self.listeners: list[Callable[[TeapotState], None]] = []
        self.state = TeapotState(count=0, full_time=0, current_time=0, iteration_time=tolerance,
                                 teapot_status=TeapotStatus.NOT_TEAPOT)

    def noise(self, level=None):
        if level is None:
            level = self._tolerance

        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                noise_value = (random.random() * level / 200) * random.choice([-1, 1])
                return result + noise_value

            return wrapper

        return decorator

    @property
    def empty(self):
        @self.noise(level=self._tolerance)
        def inner_empty():
            return 0

        return inner_empty()

    @property
    def empty_teapot(self):
        @self.noise()
        def inner_empty_teapot():
            return self.empty + self._empty_teapot_weight + self._leaves_min_weight

        return inner_empty_teapot()

    @property
    def full_teapot(self):
        @self.noise()
        def inner_full_teapot():
            return self.empty_teapot + self._water_max_weight + self._cap_weight

        return inner_full_teapot()

    @property
    def full_teapot_cap(self):
        @self.noise()
        def inner_full_teapot_cap():
            return self.empty_teapot + self._leaves_max_weight + self._water_max_weight + self._cap_weight + self._tolerance

        return inner_full_teapot_cap()

    def identify_teapot_status(self, weight):
        empty_threshold = 3

        statuses = {
            TeapotStatus.EMPTY: (-empty_threshold, empty_threshold),
            TeapotStatus.TEAPOT: (
                self._empty_teapot_weight - self._tolerance,
                self._empty_teapot_weight + self._tolerance
            ),
            TeapotStatus.TEAPOT_LEAVES: (
                self._empty_teapot_weight + self._leaves_min_weight - self._tolerance,
                self._empty_teapot_weight + self._leaves_max_weight + self._tolerance
            ),
            TeapotStatus.TEAPOT_LEAVES_CAP: (
                self._empty_teapot_weight + self._leaves_min_weight + self._cap_weight - self._tolerance,
                self._empty_teapot_weight + self._leaves_max_weight + self._cap_weight + self._tolerance
            ),
            TeapotStatus.TEAPOT_LEAVES_WATER: (
                self._empty_teapot_weight + self._leaves_min_weight + self._water_min_weight - self._tolerance,
                self._empty_teapot_weight + self._leaves_max_weight + self._water_max_weight + self._tolerance
            ),
            TeapotStatus.TEAPOT_LEAVES_WATER_CAP: (
                self._empty_teapot_weight + self._leaves_min_weight + self._water_min_weight + self._cap_weight - self._tolerance,
                self._empty_teapot_weight + self._leaves_max_weight + self._water_max_weight + self._cap_weight + self._tolerance
            ),
            TeapotStatus.TEAPOT_UNKNOWN: (
                self._empty_teapot_weight + self._leaves_max_weight + self._water_max_weight + self._cap_weight + self._tolerance,
                300
            ),
        }

        for status, (min_weight, max_weight) in statuses.items():
            if min_weight <= weight <= max_weight:
                return status

        return TeapotStatus.NOT_TEAPOT

    def add_listener(self, listener: Callable[[TeapotState], None]):
        self.listeners.append(listener)

    def remove_listener(self, listener: Callable[[TeapotState], None]):
        self.listeners.remove(listener)

    def emit(self):
        for listener in self.listeners:
            listener(self.state)

    def handle_event(self, event: AppEvent):
        if isinstance(event, StartTimer):
            self.state.count = self.state.count + 1
            self.start_timer()
        elif isinstance(event, UpdateIterationTimeEvent):
            self.state.iteration_time = self.state.iteration_time + event.iteration_time
        elif isinstance(event, UpdateCountEvent):
            self.state.count = event.count
        elif isinstance(event, UpdateStatusEvent):
            self.state.teapot_status = event.teapot_status
        self.emit()

    def start_timer(self):
        # Reset current time to 0 and increment by 1 each second
        def update_timer():
            if self.state.current_time <= self.state.iteration_time:
                self.state.current_time += 0.01
                self.emit()  # Emit updated state to listeners
                # Schedule the next timer update
                Timer(0.01, update_timer).start()
            else:
                self.state.current_time = 0
                Timer(0.1, self.emit).start()

        Timer(0.01, update_timer).start()


teapot_bloc = TeapotBloc()  # for imports todo: try singleton
