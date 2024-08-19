from typing import Callable, List
from constants import *
from app_state import AppState
from app_event import *


class AppBloc:
    def __init__(self):
        # Initialize the state with example values
        self.state = AppState(count=0, full_time=total_time, current_time=0, iteration_time=0)
        self.listeners: List[Callable[[AppState], None]] = []

    def add_listener(self, listener: Callable[[AppState], None]):
        self.listeners.append(listener)

    def remove_listener(self, listener: Callable[[AppState], None]):
        self.listeners.remove(listener)

    def emit(self):
        for listener in self.listeners:
            listener(self.state)

    def handle_event(self, event: AppEvent):
        if isinstance(event, UpdateCurrentTimeEvent):
            self.state.current_time = event.current_time
        elif isinstance(event, UpdateFullTimeEvent):
            self.state.full_time = event.full_time
        elif isinstance(event, UpdateIterationTimeEvent):
            self.state.iteration_time = event.iteration_time
        elif isinstance(event, UpdateCountEvent):
            self.state.count = event.count
        self.emit()