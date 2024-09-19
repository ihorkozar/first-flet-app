import flet as ft

from components.body_content_widget import body_content
from components.bottom_widget import bottom_widget
from components.custom_app_bar import custom_app_bar
from components.top_widget import top_widget
from utils.app_constants import *


def main(page: ft.Page):
    page.title = "Flet Scaffold"
    page.window.width = 500
    page.window.height = 820
    page.window.resizable = False
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
                bottom_widget(page)
            ],
            expand=True,
        ),
        expand=True,
    )

    page.appbar = app_bar
    page.add(body)
    page.update()


ft.app(target=main)
