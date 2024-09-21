import flet as ft
from bloc.bloc_builder import TeapotBlocBuilder
from bloc.teaport_event import StartTimer
from bloc.teapot_bloc import *
from components.stepper_button import StepperButton
from flet_core import MainAxisAlignment, TextAlign
from utils.app_constants import *

from utils.app_constants import white


def should_rebuild_count(prev_state: TeapotState, new_state: TeapotState) -> bool:
    return prev_state.count != new_state.count


def should_rebuild_count_and_leaf(prev_state: TeapotState, new_state: TeapotState) -> bool:
    return prev_state.count != new_state.count or prev_state.leaf != new_state.leaf


def should_rebuild_iteration_time(prev_state: TeapotState, new_state: TeapotState) -> bool:
    return prev_state.iteration_time != new_state.iteration_time


def increment_time():
    teapot_bloc.handle_event(UpdateIterationTimeEvent(5))


def decrement_time():
    teapot_bloc.handle_event(UpdateIterationTimeEvent(-5))


def bottom_widget(page: ft.Page):
    return ft.Row(
        [
            TeapotBlocBuilder(
                control=ft.Container(),
                bloc=teapot_bloc,
                build_when=should_rebuild_count_and_leaf,
                builder=lambda state: ft.OutlinedButton(
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(16, 16, 16, 16), ),
                        side=ft.BorderSide(
                            color=silver if state.leaf == 0 else button_color,
                            width=1
                        ),
                    ),
                    height=60,
                    width=80,
                    content=ft.Icon(ft.icons.ARROW_RIGHT, color=white),
                    on_click=lambda e: handle_start_timer(teapot_bloc, state, page),
                    disabled=state.cup == 0
                ),
            ).build(),

            TeapotBlocBuilder(
                control=ft.Container(),
                bloc=teapot_bloc,
                build_when=should_rebuild_count,
                builder=lambda state: ft.OutlinedButton(
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(16, 16, 16, 16), ),
                        side=ft.BorderSide(
                            color=button_color,
                            width=1
                        ),
                    ),
                    height=60,
                    width=80,
                    content=ft.Image(
                        src="../assets/tea.svg",
                    ),
                    on_click=lambda e: teapot_bloc.handle_event(StartStreamEvent())
                ),
            ).build(),
            TeapotBlocBuilder(
                control=ft.Container(),
                bloc=teapot_bloc,
                build_when=should_rebuild_iteration_time,
                builder=lambda state: StepperButton(
                    on_left_click=lambda: decrement_time() if state.iteration_time >= 10 else None,
                    on_right_click=increment_time,
                    button_color=button_color,
                    text_color=button_color2,
                ),
            ).build(),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=8,
    )


def handle_start_timer(bloc, state, page):
    if state.count < 12:
        bloc.handle_event(StartTimer())
    else:
        show_count_exceeds_dialog(page)


def show_count_exceeds_dialog(page: ft.Page):
    dialog = ft.AlertDialog(
        bgcolor=dialog_bg,
        actions_alignment=MainAxisAlignment.SPACE_BETWEEN,
        title=ft.Row(
            expand=True,
            alignment=MainAxisAlignment.END,
            controls=[ft.IconButton(ft.icons.CLOSE, on_click=lambda e: close_dialog(page), icon_color=white)],
        ),
        content=ft.Container(
            width=100,
            height=60,
            content=ft.Text("Do you want to make a new cup?",
                            text_align=TextAlign.CENTER,
                            style=ft.TextStyle(size=16)),
        ),
        actions=[
            ft.OutlinedButton("Enough", on_click=lambda _: close_dialog(page, False), style=ft.ButtonStyle(
                color=white,
                shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(16, 16, 16, 16), ),
                side=ft.BorderSide(
                    color=button_color,
                    width=1
                ),
            ), height=60),
            ft.ElevatedButton("One more", on_click=lambda _: close_dialog(page, True), style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(16, 16, 16, 16), ),
                bgcolor=button_color,
                color=button_color2,
            ), height=60),
        ]
    )

    def close_dialog(page: ft.Page, new_cup: bool):
        if new_cup:
            teapot_bloc.handle_event(StartCupEvent())
        dialog.open = False  # Close the dialog
        page.update()  # Update the page to reflect the change

    page.dialog = dialog  # Assign the dialog to the page's dialog property
    page.dialog.open = True  # Open the dialog
    page.update()
