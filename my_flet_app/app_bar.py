import flet as ft
from constants import *

def create_app_bar():
    return ft.AppBar(
        title=ft.Text("New set"),
        center_title=True,
        bgcolor=main_color,
        leading=ft.Image(src="assets/back.svg"),
        actions=[ft.Image(src="assets/more.svg")],
    )
