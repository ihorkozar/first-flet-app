from copy import deepcopy

import flet as ft
from typing import Callable, TypeVar, Generic, Optional

from teapot_bloc import *
from teapot_state import *


class TeapotBlocBuilder(TeapotState):
    def __init__(
            self,
            bloc: TeapotBloc,
            builder: Callable[[TeapotState], ft.Control],
            control: ft.Control,
            build_when: Optional[Callable[[TeapotState, TeapotState], bool]]):
        super().__init__(bloc.state.count, bloc.state.full_time, bloc.state.current_time, bloc.state.iteration_time,
                         bloc.state.teapot_status, )
        print("TeapotBlocBuilder __init__")
        self.bloc = bloc
        self.builder = builder
        self.control = control
        self.build_when = build_when
        self.previous_state = deepcopy(bloc.state)

        # Add listener to the Bloc
        self.bloc.add_listener(self._on_state_change)

    def _on_state_change(self, new_state: TeapotState):
        """Rebuild the widget when the state changes."""
        print(f"new_state {new_state.current_time}")
        print(f"self.previous_state {self.previous_state.current_time}")

        # Check build_when
        if self.build_when is None or self.build_when(self.previous_state, new_state):
            self.control.content = self.builder(new_state)
            self.control.update()

        self.previous_state = deepcopy(new_state)

    def build(self):
        """Initial build based on the current state."""
        self.control.content = self.builder(self.bloc.state)
        return self.control
