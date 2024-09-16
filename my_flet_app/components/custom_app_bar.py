import flet as ft

from utils.app_constants import *


def custom_app_bar():
    return ft.AppBar(
        title=ft.Text("New set", color=yellow),
        center_title=True,
        bgcolor=main_color,
        leading=ft.IconButton(
            content=ft.Image(src="../assets/back.svg"),
            on_click=lambda e: print("Back button pressed")
        ),
        actions=[
            ft.IconButton(
                content=ft.Image(src="../assets/more.svg"),
                on_click=lambda e: print("More button pressed")
            )
        ]
    )
