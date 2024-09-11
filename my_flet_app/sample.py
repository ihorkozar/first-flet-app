
import flet as ft
from typing import Callable, TypeVar, Generic

# Reusing the Bloc and BlocBuilder definitions
S = TypeVar('S')


class Bloc(Generic[S]):
    def __init__(self, initial_state: S):
        self._state = initial_state
        self._listeners: list[Callable[[S], None]] = []

    @property
    def state(self) -> S:
        return self._state

    def set_state(self, new_state: S):
        self._state = new_state
        self._emit()

    def add_listener(self, listener: Callable[[S], None]):
        self._listeners.append(listener)

    def remove_listener(self, listener: Callable[[S], None]):
        self._listeners.remove(listener)

    def _emit(self):
        for listener in self._listeners:
            listener(self._state)


class BlocBuilder(Generic[S]):
    def __init__(self, bloc: Bloc[S], builder: Callable[[S], ft.Control], control: ft.Control):
        self.bloc = bloc
        self.builder = builder
        self.control = control

        # Add listener to the Bloc
        self.bloc.add_listener(self._on_state_change)

    def _on_state_change(self, state: S):
        """Rebuild the widget when the state changes."""
        # Update the control content
        self.control.content = self.builder(state)
        self.control.update()

    def build(self):
        """Initial build based on the current state."""
        self.control.content = self.builder(self.bloc.state)
        return self.control


# Counter Bloc
class CounterBloc(Bloc[int]):
    def increment(self):
        self.set_state(self.state + 1)


# Custom widget that includes BlocBuilder
class CounterWidget(ft.UserControl):
    def __init__(self, counter_bloc: CounterBloc):
        super().__init__()
        self.counter_bloc = counter_bloc
        self.column = ft.Container()

    def build(self):
        return ft.Column(
            [
                BlocBuilder(
                    bloc=self.counter_bloc,
                    builder=lambda state: ft.Text(f"Counter: {state}", size=30),
                    control=self.column  # Pass the container to be updated
                ).build(),
                ft.ElevatedButton("Increment", on_click=self.increment_counter)
            ]
        )

    def increment_counter(self, e):
        self.counter_bloc.increment()


# Main function for the Flet app
def main(page: ft.Page):
    counter_bloc = CounterBloc(0)

    # Use the CounterWidget, which includes BlocBuilder
    counter_widget = CounterWidget(counter_bloc)

    page.add(counter_widget)
    page.update()


# Start the Flet app
ft.app(target=main)
