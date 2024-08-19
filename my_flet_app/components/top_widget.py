import flet as ft
from my_flet_app.constants import *

def top_widget():
    return ft.Container(
        padding=ft.Padding(10, 16, 10, 16),
        content=ft.Row(
            height=56,
            alignment=ft.MainAxisAlignment.CENTER,  # Center the row contents
            spacing=10,
            controls=[
                ft.Row(
                    width=80,
                    controls=[
                        ft.Image(
                            src="assets/cup.svg",
                            color=divider_color,
                            width=24
                        ),
                        ft.Text("100 g", size=14, color=divider_color)
                        # Text next to the cup icon
                    ],
                ),
                ft.VerticalDivider(width=1, color=divider_color),
                ft.Row(
                    width=80,
                    controls=[
                        ft.Image(
                            src="assets/leaf.svg",
                            color=divider_color,
                            width=24
                        ),
                        ft.Text("2 g", size=14, color=divider_color)
                        # Text next to the leaf icon
                    ],
                ),
                ft.VerticalDivider(width=1, color=divider_color),
                ft.Row(
                    width=80,
                    controls=[
                        ft.Image(
                            src="assets/icon_water.svg",
                            color=divider_color,
                            width=24
                        ),
                        ft.Text("150 ml", size=14, color=divider_color)
                        # Text next to the water icon
                    ],
                ),
                ft.VerticalDivider(width=1, color=divider_color),
                ft.Row(
                    width=80,
                    controls=[
                        ft.Image(
                            src="assets/lid.svg",
                            color=divider_color,
                            width=24
                        ),
                        ft.Text("0 g", size=14, color=divider_color)
                        # Text next to the lid icon
                    ],
                ),
            ]
        ),
        border=ft.Border(
            top=ft.BorderSide(color=divider_color, width=1),  # Set the top border
            bottom=ft.BorderSide(color=divider_color, width=1)  # Set the bottom border
        )
    )
