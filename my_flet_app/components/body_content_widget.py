import flet as ft
from bloc.bloc_builder import TeapotBlocBuilder
from bloc.teapot_bloc import teapot_bloc
from bloc.teapot_state import TeapotStatus, TeapotState
from components.circular_progress_widget import circular_progress_widget
from flet_core import MainAxisAlignment
from utils.app_constants import *


def should_rebuild_count(prev_state: TeapotState, new_state: TeapotState) -> bool:
    return prev_state.count != new_state.count


def should_rebuild_time(prev_state: TeapotState, new_state: TeapotState) -> bool:
    return (prev_state.current_time != new_state.current_time or
            prev_state.iteration_time != new_state.iteration_time or
            prev_state.teapot_status != new_state.teapot_status)


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
                builder=lambda state:
                ft.Column(
                    height=480,
                    width=80,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(f"{state.count}", color=yellow),
                                ft.Text("/12"),
                            ],
                            spacing=0
                        ),
                        water_icons(state),
                        ft.Text(f"{state.count * 150} ml", style=ft.TextStyle(color=yellow)),
                    ],
                ),
            ).build(),
            ft.Container(width=26),
            TeapotBlocBuilder(
                control=ft.Container(),
                bloc=teapot_bloc,
                build_when=should_rebuild_time,
                builder=lambda state:
                ft.Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        circular_progress_widget(state.current_time, state.iteration_time, state.full_time),
                        ft.Container(height=26),
                        build_teapot_image(state)
                    ]),
            ).build()
        ])


def water_icons(state):
    icons = []
    for i in range(12):
        color = orange if i < state.count else silver
        icons.append(
            ft.Icon(ft.icons.WATER_DROP, color=color),
        )
    return ft.Column(controls=icons)


def build_teapot_image(state):
    if state.teapot_status == TeapotStatus.NOT_TEAPOT or state.teapot_status == TeapotStatus.EMPTY:
        return ft.Container()
    elif state.teapot_status == TeapotStatus.TEAPOT:
        return ft.Image(
            src="assets/cup-empty.png",
            width=195,
            height=195,
        )
    else:
        return ft.Image(
            src="assets/cup-open.png" if state.current_time == 0 else "assets/cup-close.png",
            width=195,
            height=195,
        )
