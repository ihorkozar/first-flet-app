import flet as ft
from bloc.bloc_builder import TeapotBlocBuilder
from bloc.teaport_event import StartTimer
from bloc.teapot_bloc import *
from utils.app_constants import *


def should_rebuild_count(prev_state: TeapotState, new_state: TeapotState) -> bool:
    return prev_state.count != new_state.count


def bottom_widget(page: ft.Page):
    return ft.Row(
        [
            ft.OutlinedButton(
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
                    src="../assets/stop.svg",
                ),
                on_click=lambda e: print("Outlined Button 1 clicked"),
            ),
            TeapotBlocBuilder(
                control=ft.Container(),
                bloc=teapot_bloc,
                build_when=should_rebuild_count,
                builder=lambda state:
                ft.OutlinedButton(
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
                    on_click=lambda e: handle_start_timer(teapot_bloc, state, page)
                ),
            ).build(),

            ft.ElevatedButton(
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(16, 16, 16, 16), ),
                    bgcolor=button_color,
                    color=button_color2,
                ),
                height=60,
                width=179,
                content=ft.Row(
                    width=80,
                    alignment=ft.alignment.center,
                    controls=[
                        ft.Image(
                            src="../assets/update.svg",
                        ),
                        ft.Text("+5 sec")
                    ]),
                on_click=lambda e: teapot_bloc.handle_event(UpdateIterationTimeEvent(5)),
            ),
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
    def close_dialog(_):
        page.dialog.open = False  # Close the dialog
        page.close(dialog)

    dialog = ft.AlertDialog(
        title=ft.Text("Count Exceeds Limit"),
        content=ft.Text("You cannot start the timer because the count exceeds 12."),
        actions=[
            ft.TextButton("OK", on_click=close_dialog)
        ]
    )
    page.open(dialog)
