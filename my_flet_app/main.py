import threading

import flet as ft
from flet_core import MainAxisAlignment, theme

from constants import *
from app_bar import create_app_bar
from weights import start_timer


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

    progress_ring = ft.ProgressRing(
        value=1,
        width=195,
        height=195,
        stroke_width=14,
        color=yellow,
        bgcolor=silver,
    )

    remaining_time_text = ft.Text(
        f"{total_time} s left",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        font_family="InknutAntiqua"
    )

    teapot_state_text = ft.Column(controls=[
        remaining_time_text,
        ft.Text(
            "State: unknown",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLACK,
        )
    ])

    # Stack the ProgressRing and the Text together
    circular_indicator = ft.Stack(
        [
            progress_ring,
            ft.Container(content=teapot_state_text, alignment=ft.alignment.center)
        ],
        alignment=ft.alignment.center
    )

    button_row = ft.Row(
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
                    src="assets/stop.svg",
                ),
                on_click=lambda e: print("Outlined Button 1 clicked"),
            ),
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
                    src="assets/tea.svg",
                ),
                on_click=lambda e: print("Outlined Button 2 clicked"),
            ),
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
                            src="assets/update.svg",
                        ),
                        ft.Text("+5 sec")
                    ]),
                on_click=lambda e: print("Elevated Button clicked"),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=8,  # Space between buttons
    )

    top_widget = ft.Container(
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

    content_widget = ft.Row(width=380, alignment= ft.MainAxisAlignment.CENTER, vertical_alignment= ft.CrossAxisAlignment.START, controls=[
        ft.Column(width=56,  controls=[
            ft.Text("3 /12"),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),
            ft.Image(
                src="assets/icon_water.svg",
                color="#FAD074",
                width=24
            ),

        ]),
        ft.Container(width=26),
        ft.Column(controls=[
            circular_indicator,
            ft.Container(height=45),
            ft.Image(
                src="assets/cup-open.png",
                width=195
            ),
        ])
    ])

    # Create the Body (Content area)
    body = ft.Container(
        content=ft.ListView(
            [
                top_widget,
                ft.Container(height=45),
                content_widget,
                ft.Container(height=45),
                button_row,
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
    threading.Thread(target=start_timer, args=(page, progress_ring, remaining_time_text, teapot_state_text)).start()


# Run the Flet app
ft.app(target=main)
