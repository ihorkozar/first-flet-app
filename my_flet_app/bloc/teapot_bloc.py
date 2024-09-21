from threading import Timer
from typing import Callable

import rx
import rx.operators as ops
from bloc.teaport_event import *
from bloc.teapot_state import TeapotStatus, TeapotState
from utils.app_constants import tolerance
from weights import *


class TeapotBloc:
    def __init__(self):
        self.listeners: list[Callable[[TeapotState], None]] = []
        self.state = TeapotState(count=0, full_time=0, current_time=0, iteration_time=tolerance,
                                 teapot_status=TeapotStatus.NOT_TEAPOT, cup=0, leaf=0, water=0, lid=0,
                                 is_time_alarm=False)

    def add_listener(self, listener: Callable[[TeapotState], None]):
        self.listeners.append(listener)

    def remove_listener(self, listener: Callable[[TeapotState], None]):
        self.listeners.remove(listener)

    def emit(self):
        if self.state is None:
            print("State is None, cannot emit updates")
            return

        for listener in self.listeners:
            listener(self.state)

    def handle_event(self, event: AppEvent):
        if isinstance(event, StartTimer):
            self.state.water = 0
            self.state.lid = 0
            self.state.count = self.state.count + 1
            self.state.is_time_alarm = False
            stream = rx.create(proceed_stream)
            stream.subscribe(
                on_next=lambda value: self.handle_event(UpdateWeightEvent(weight=value)),
                on_error=lambda e: print(f"Error: {e}"),
                on_completed=lambda: print("End")
            )
            lid_stream = rx.interval(0.1).pipe(  # This interval checks every 0.1 seconds
                ops.map(lambda _: self.state.lid),  # Emit current lid value
                ops.filter(lambda lid: lid != 0),  # Proceed only if lid is non-zero
                ops.take(1)  # Take only the first value when lid is not 0
            )

            # Subscribe to lid_stream and start the timer when lid != 0
            lid_stream.subscribe(
                on_next=lambda _: self.start_timer(),
                on_error=lambda e: print(f"Error: {e}")
            )
        elif isinstance(event, StartStreamEvent):
            if hasattr(self, '_timer'):
                self._timer.cancel()
            self.state.is_time_alarm = False
            self.state.water = 0
            self.state.cup = 0
            self.state.leaf = 0
            self.state.lid = 0
            self.state.count = 0
            self.state.full_time = 0
            self.state.current_time = 0
            stream = rx.create(initial_stream)
            stream.subscribe(
                on_next=lambda value: self.handle_event(UpdateWeightEvent(weight=value)),
                on_error=lambda e: print(f"Error: {e}"),
                on_completed=lambda: print("End")
            )
        elif isinstance(event, UpdateIterationTimeEvent):
            self.state.iteration_time = self.state.iteration_time + event.iteration_time
        elif isinstance(event, UpdateCountEvent):
            self.state.count = event.count
        elif isinstance(event, UpdateStatusEvent):
            self.state.teapot_status = event.teapot_status
        elif isinstance(event, UpdateWeightEvent):
            new_status = identify_teapot_state(event.weight)
            print(event.weight)
            self.state.teapot_status = new_status
            if new_status == TeapotStatus.TEAPOT:
                self.state.cup = event.weight
            elif new_status == TeapotStatus.TEAPOT_LEAVES:
                self.state.leaf = event.weight - self.state.cup
            elif new_status == TeapotStatus.TEAPOT_LEAVES_CAP:
                self.state.leaf = event.weight - self.state.cup
            elif new_status == TeapotStatus.TEAPOT_LEAVES_WATER:
                self.state.water = event.weight - self.state.cup - self.state.leaf
            elif new_status == TeapotStatus.TEAPOT_LEAVES_WATER_CAP:
                self.state.lid = event.weight - self.state.cup - self.state.leaf - self.state.water

        self.emit()

    def start_timer(self):
        # Stop any existing timer
        if hasattr(self, '_timer'):
            self._timer.cancel()
            self.state.full_time += self.state.current_time

        # Reset current time before starting
        self.state.current_time = 0

        def update_timer():
            if self.state.current_time < self.state.iteration_time:
                self.state.current_time += 0.01
                self.emit()
                self._timer = Timer(0.01, update_timer)
                self._timer.start()
            else:
                self.state.full_time += self.state.iteration_time
                self.state.current_time = 0
                self.state.is_time_alarm = True
                self.emit()

        # Start the timer
        self._timer = Timer(0.01, update_timer)
        self._timer.start()


teapot_bloc = TeapotBloc()  # for imports todo: try singleton
