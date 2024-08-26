import flet as ft

from app_constants import silver, yellow, total_time
from utils import format_minutes


def circular_progress_widget():
    progress_ring = ft.ProgressRing(
        value=1,
        width=195,
        height=195,
        stroke_width=22,
        color=silver,
        bgcolor=yellow,
    )

    remaining_time_text = ft.Text(
        format_minutes(0),
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        font_family="InknutAntiqua"
    )

    constant_time_text = ft.Text(
        format_minutes(total_time / 12),
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        font_family="InknutAntiqua"
    )

    full_time_text = ft.Text(
        format_minutes(0),
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
    )

    text_data = ft.Column(controls=[
        remaining_time_text,
        constant_time_text,
        full_time_text
    ])

    return ft.Stack(
        [
            progress_ring,
            ft.Container(content=text_data, alignment=ft.alignment.center)
        ],
        alignment=ft.alignment.center
    )
