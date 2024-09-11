import flet as ft
from flet_core import MainAxisAlignment

from circular_progress_widget import circular_progress_widget
from bloc_builder import TeapotBlocBuilder
from teapot_bloc import teapot_bloc


def body_content():
    return TeapotBlocBuilder(
        control= ft.Container(),
        bloc=teapot_bloc,
        builder=lambda state: ft.Row(width=380, alignment=ft.MainAxisAlignment.CENTER,
                                     vertical_alignment=ft.CrossAxisAlignment.START, controls=[
                ft.Column(width=56, horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                    ft.Text(f"{state.count} /12"),
                    *[
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=32
                        ) for _ in range(state.count)  # Display images based on count
                    ],
                    *[
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#ffffff",
                            width=32
                        ) for _ in range(12 - state.count)  # Display images based on count
                    ],

                ]),
                ft.Container(width=26),
                ft.Column(alignment=MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          controls=[
                              circular_progress_widget(),
                              ft.Image(
                                  src="assets/cup-open.png",
                                  width=195
                              ),
                          ])
            ])
    )
