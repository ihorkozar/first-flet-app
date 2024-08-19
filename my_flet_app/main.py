import flet as ft
from constants import *
from components.body_content_widget import body_content_widget
from components.app_bar import create_app_bar
from components.bottom_widget import bottom_widget
from components.top_widget import top_widget

def main(page: ft.Page):
    # Set the title of the app
    page.title = "Flet Scaffold Example"
    page.bgcolor = main_color
    page.fonts = {
        "InknutAntiqua": "fonts/InknutAntiqua-Medium.ttf",
    }

    page.theme = ft.Theme(font_family="InknutAntiqua")

    # Create an AppBar
    app_bar = create_app_bar()

    # Create the Body (Content area)
    body = ft.Container(
        content=ft.ListView(
            [
                top_widget,
                ft.Container(height=45),
                body_content_widget,
                ft.Container(height=45),
                bottom_widget(
                    lambda e: print("x")),
            ],
            expand=True,
        ),
        expand=True,
    )

    # Add AppBar, Body, and FAB to the page
    page.appbar = app_bar
    page.add(body)

    # Update the page
    page.update()


# Run the Flet app
ft.app(target=main)
