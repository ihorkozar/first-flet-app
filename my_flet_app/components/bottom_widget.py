import flet as ft

from my_flet_app.constants import *


def bottom_widget(on_start_click: ft.OptionalEventCallable):
    return ft.Row(
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
                on_click=on_start_click,
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
