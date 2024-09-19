import flet as ft
from bloc.bloc_builder import TeapotBlocBuilder
from bloc.teapot_bloc import teapot_bloc
from bloc.teapot_state import TeapotState
from utils.app_constants import *
from utils.utils import with_opacity


def top_section_element(icon_src: str, text: str, is_active: bool):
    text_color = yellow if is_active else with_opacity(yellow, 0.5)
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        width=80,
        controls=[
            ft.Image(
                src=icon_src,
                color=text_color,
                width=20
            ),
            ft.Text(text, size=14, color=text_color)
        ]
    )


def should_rebuild(prev_state: TeapotState, new_state: TeapotState) -> bool:
    return (prev_state.cup != new_state.cup or
            prev_state.water != new_state.water or
            prev_state.leaf != new_state.leaf or
            prev_state.lid != new_state.lid)

def top_widget():
    return ft.Container(
        padding=ft.Padding(10, 16, 10, 16),
        content=TeapotBlocBuilder(
            control=ft.Container(),
            bloc=teapot_bloc,
            build_when=should_rebuild,
            builder=lambda state: ft.Row(
                height=56,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    top_section_element(icon_src="../assets/cup.svg", text=f"{int(state.cup)} g",
                                        is_active=state.cup != 0),
                    ft.VerticalDivider(width=1, color=divider_color),
                    top_section_element(icon_src="../assets/leaf.svg", text=f"{int(state.leaf)} g",
                                        is_active=state.leaf != 0),
                    ft.VerticalDivider(width=1, color=divider_color),
                    top_section_element(icon_src="../assets/icon_water.svg", text=f"{int(state.water)} ml",
                                        is_active=state.water != 0),
                    ft.VerticalDivider(width=1, color=divider_color),
                    top_section_element(icon_src="../assets/lid.svg", text=f"{int(state.lid)} g",
                                        is_active=state.lid != 0),
                ]
            )

        ).build(),
        border=ft.Border(
            top=ft.BorderSide(color=divider_color, width=1),
            bottom=ft.BorderSide(color=divider_color, width=1)
        )
    )
