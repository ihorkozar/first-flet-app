import flet as ft

from app_constants import silver, yellow, total_time
from utils import format_minutes


def circular_progress_widget(current_time, iteration_time):
    progress_value = current_time / iteration_time if iteration_time > 0 else 0
    progress_ring = ft.ProgressRing(
        value=progress_value,
        width=195,
        height=195,
        stroke_width=22,
        color=silver,
        bgcolor=yellow,
    )

    remaining_time_text = ft.Text(
        format_minutes(current_time),
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
