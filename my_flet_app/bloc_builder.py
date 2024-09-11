import flet as ft
from typing import Callable, TypeVar, Generic

from teapot_bloc import *
from teapot_state import *


class TeapotBlocBuilder(TeapotState):
    def __init__(self, bloc: TeapotBloc, builder: Callable[[TeapotState], ft.Control], control: ft.Control):
        self.bloc = bloc
        self.builder = builder
        self.control = control

        # Add listener to the Bloc
        self.bloc.add_listener(self._on_state_change)

    def _on_state_change(self, state: TeapotState):
        """Rebuild the widget when the state changes."""
        # Update the control content
        self.control.content = self.builder(state)
        self.control.update()

    def build(self):
        """Initial build based on the current state."""
        self.control.content = self.builder(self.bloc.state)
        return self.control