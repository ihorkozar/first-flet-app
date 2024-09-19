import flet as ft

from utils.app_constants import silver, yellow, white
from utils.utils import format_minutes


def circular_progress_widget(current_time, iteration_time, full_time, is_time_alarm):
    progress_value = current_time / iteration_time if iteration_time > 0 else 0
    progress_ring = ft.ProgressRing(
        value=1 - progress_value,
        width=195,
        height=195,
        stroke_width=16,
        color=ft.colors.RED if is_time_alarm else yellow,
        bgcolor=silver,
        stroke_cap=ft.StrokeCap.ROUND,
    )

    static_grey_ring = ft.ProgressRing(
        value=1.0,
        width=195,
        height=195,
        stroke_width=22,
        color=silver,
        bgcolor=silver,
    )

    remaining_time_text = ft.Text(
        format_minutes(current_time),
        size=36,
        color=yellow,
        font_family="InknutAntiqua"
    )

    constant_time_text = ft.Text(
        format_minutes(iteration_time),
        size=16,
        color=white,
        font_family="InknutAntiqua"
    )

    full_time_text = ft.Text(
        format_minutes(full_time),
        size=16,
        color=white,
        font_family="InknutAntiqua"
    )

    text_data = ft.Column(
        controls=[
            remaining_time_text,
            ft.Container(height=1, width=80, bgcolor=white),
            constant_time_text,
            ft.Container(height=1, width=80, bgcolor=white),
            full_time_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return ft.Stack(
        [
            static_grey_ring,
            progress_ring,
            text_data
        ],
        alignment=ft.alignment.center
    )
