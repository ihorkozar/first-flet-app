import time

import flet as ft

from app_constants import *
from body_content_widget import body_content
from custom_app_bar import custom_app_bar
from bottom_widget import bottom_widget
from top_widget import top_widget

def main(page: ft.Page):
    page.title = "Flet Scaffold"
    page.window.width = 500
    page.window.height = 820
    page.window_resizable = False
    page.bgcolor = main_color
    page.fonts = {
        "InknutAntiqua": "fonts/InknutAntiqua-Medium.ttf",
    }

    page.theme = ft.Theme(font_family="InknutAntiqua")

    app_bar = custom_app_bar()

    body = ft.Container(
        content=ft.ListView(
            [
                top_widget(),
                ft.Container(height=32),
                body_content(),
                ft.Container(height=32),
                bottom_widget()
            ],
            expand=True,
        ),
        expand=True,
    )

    page.appbar = app_bar
    page.add(body)
    page.update()

ft.app(target=main)

