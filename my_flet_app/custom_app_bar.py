import flet as ft
from app_constants import *

def custom_app_bar():
    return ft.AppBar(
        title=ft.Text("New set", color=yellow),
        center_title=True,
        bgcolor=main_color,
        leading=ft.Image(src="assets/back.svg"),
        actions=[ft.Image(src="assets/more.svg")],
    )
