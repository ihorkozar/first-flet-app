import flet as ft
from flet_core import MainAxisAlignment

from my_flet_app.components.circular_progress_widget import circular_progress_widget


def body_content_widget():
    return ft.Row(width=380, alignment=ft.MainAxisAlignment.CENTER,
                  vertical_alignment=ft.CrossAxisAlignment.START, controls=[
            ft.Column(width=56, horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                ft.Text("3 /12"),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),
                ft.Image(
                    src="assets/icon_water.svg",
                    color="#FAD074",
                    width=32
                ),

            ]),
            ft.Container(width=26),
            ft.Column(alignment=MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                circular_progress_widget,
                ft.Image(
                    src="assets/cup-open.png",
                    width=195
                ),
            ])
        ])
