import flet as ft
from flet_core import MainAxisAlignment

from circular_progress_widget import circular_progress_widget
from bloc_builder import TeapotBlocBuilder
from app_constants import *
from teapot_state import TeapotState
from teapot_bloc import teapot_bloc


def should_rebuild_count(prev_state: TeapotState, new_state: TeapotState) -> bool:
    return prev_state.count != new_state.count


def should_rebuild_time(prev_state: TeapotState, new_state: TeapotState) -> bool:
    return prev_state.current_time != new_state.current_time


def body_content():
    return ft.Row(
        width=380,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
        controls=[
            TeapotBlocBuilder(
                control=ft.Container(),
                bloc=teapot_bloc,
                build_when=should_rebuild_count,
                builder=lambda state: ft.Column(
                    width=56,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(f"{state.count} /12"),
                        *[
                            ft.Image(
                                src="assets/icon_water.svg",
                                color=orange,
                                width=28
                            ) for _ in range(state.count)
                        ],
                        *[
                            ft.Image(
                                src="assets/icon_water.svg",
                                color=silver,
                                width=28
                            ) for _ in range(12 - state.count)
                        ],
                    ]),
            ).build(),
            ft.Container(width=26),
            TeapotBlocBuilder(
                control=ft.Container(),
                bloc=teapot_bloc,
                build_when=should_rebuild_time,
                builder=lambda state: ft.Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        circular_progress_widget(state.current_time, state.iteration_time),
                        ft.Image(
                            src="assets/cup-open.png" if state.current_time == 0 else "assets/cup-close.png",
                            width=195
                        ),
                    ]),
            ).build(),
        ]),
