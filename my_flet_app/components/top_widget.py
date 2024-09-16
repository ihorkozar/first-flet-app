import flet as ft

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

def top_widget():
    return ft.Container(
        padding=ft.Padding(10, 16, 10, 16),
        content=ft.Row(
            height=56,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                top_section_element(icon_src="../assets/cup.svg", text="100 g", is_active=True),
                ft.VerticalDivider(width=1, color=divider_color),
                top_section_element(icon_src="../assets/leaf.svg", text="2 g", is_active=False),
                ft.VerticalDivider(width=1, color=divider_color),
                top_section_element(icon_src="../assets/icon_water.svg", text="150 ml", is_active=False),
                ft.VerticalDivider(width=1, color=divider_color),
                top_section_element(icon_src="../assets/lid.svg", text="0 g", is_active=False),
            ]
        ),
        border=ft.Border(
            top=ft.BorderSide(color=divider_color, width=1),
            bottom=ft.BorderSide(color=divider_color, width=1)
        )
    )
