import flet as ft
from flet_core import MainAxisAlignment


class StepperButton(ft.UserControl):
    def __init__(self, on_left_click, on_right_click, button_color, text_color):
        super().__init__()
        self.on_left_click = on_left_click
        self.on_right_click = on_right_click
        self.button_color = button_color
        self.text_color = text_color

    def build(self):
        return ft.Container(
            height=60,
            width=180,
            bgcolor=self.button_color,
            border_radius=ft.border_radius.all(16),
            content=ft.Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=40,
                        height=60,
                        ink=True,
                        on_click=lambda e: self.on_left_click(),
                        content=ft.Icon(ft.icons.REMOVE, color=self.text_color)
                    ),
                    ft.Row(
                        width=80,
                        alignment=ft.alignment.center,
                        controls=[
                            ft.Image(
                                src="../assets/update.svg",
                            ),
                            ft.Text("+5 sec", color=self.text_color)
                        ]),
                    ft.Container(
                        width=40,
                        height=60,
                        ink=True,
                        on_click=lambda e: self.on_right_click(),
                        content=ft.Icon(ft.icons.ADD, color=self.text_color)
                    ),
                ],
            ),
        )
