import flet as ft
from typing import Callable, TypeVar, Generic, Optional

from teapot_bloc import *
from teapot_state import *


class TeapotBlocBuilder(TeapotState):
    def __init__(
            self,
            bloc: TeapotBloc, builder: Callable[[TeapotState], ft.Control],
            control: ft.Control,
            build_when: Optional[Callable[[TeapotState, TeapotState], bool]]):
        self.bloc = bloc
        self.builder = builder
        self.control = control
        self.build_when = build_when

        # Add listener to the Bloc
        self.bloc.add_listener(self._on_state_change)

    def _on_state_change(self, state: TeapotState):
        """Rebuild the widget when the state changes."""
        if self.build_when is None or self.build_when(self.bloc.state, state):
            # Update the control content
            self.control.content = self.builder(state)
            self.control.update()

    def build(self):
        """Initial build based on the current state."""
        self.control.content = self.builder(self.bloc.state)
        return self.control
