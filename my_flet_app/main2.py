import subprocess
import threading
import time

import flet as ft
import rx
from reactivex import operators as ops
from sandbox.flet.timer_ui import TimerUI
from utils.weights import empty, empty_teapot, full_teapot, full_teapot_cap, identify_teapot_state


def update_ui(component, value, property='value'):
    setattr(component, property, value)
    component.parent.update()


def format_seconds(seconds):
    sign = "-" if seconds < 0 else ""

    abs_seconds = abs(seconds)

    hours = abs_seconds // 3600
    minutes = (abs_seconds % 3600) // 60
    secs = abs_seconds % 60

    if hours > 0:
        return f"{sign}{hours:02}:{minutes:02}:{secs:02}"
    else:
        return f"{sign}{minutes:02}:{secs:02}"


def format_statistics(stats):
    session_timer, state, weight = stats
    weight = float(weight)
    v = [f"{session_timer:02} sec", f"{weight:.1f} gr.", f"{state}"]
    if 'water' in state:
        v.append(f"Left: {session_timer:02} sec")
    print(v)
    return ",\n".join(v)
    return str(stats)


def state2filename(state):
    str = 'empty' if state == {'empty'} else 'tea_cup'
    str += '+water' if 'water' in state else ''
    str += '+cap' if 'cap' in state else ''

    return str + '.png'


def create_countdown(countdown_timer, start_from=10):
    return countdown_timer.pipe(
        ops.scan(lambda acc, _: acc - 1, start_from),
    )


def numbers_stream(observer, scheduler):
    def emit():
        observer.on_next(0.)
        values = [
            (empty, 2),
            (empty_teapot, 1),
            (full_teapot, 3),
            (full_teapot_cap, 3),
            (empty_teapot, 2),
            (full_teapot, 18),
            (empty, 4),
        ]
        delay = 0.1

        for func, count in values:
            for _ in range(int(count / delay)):
                observer.on_next(func())
                time.sleep(delay)

        observer.on_completed()

    threading.Thread(target=emit).start()


def main(page: ft.Page):
    page.title = "Timer"

    page.window.min_width = 340
    page.window.min_height = 556
    page.window.max_width = 360
    page.window.max_height = 600

    page.window.width = page.window.min_width
    page.window.height = page.window.min_height

    ui = TimerUI()
    page.add(ui)

    def on_resize(e):
        print(f"Size: {page.window.width} x {page.window.height}")

    def on_window_close(e):
        page.window.close_confirm = True

    page.on_resized = on_resize
    page.on_close = on_window_close

    timer = rx.interval(1).pipe(ops.publish())
    weight = rx.create(numbers_stream).pipe(ops.publish())
    state = weight.pipe(
        ops.map(lambda v: identify_teapot_state(v)),
        ops.distinct_until_changed(),
    )
    water_filled = state.pipe(
        ops.map(lambda s: 'water' in s),
        ops.distinct_until_changed(),
        ops.share()
    )
    trigger_start = water_filled.pipe(
        ops.filter(lambda x: x),
        ops.do_action(lambda x: print(f"trigger_start")),
        ops.share()
    )
    trigger_stop = water_filled.pipe(
        ops.filter(lambda x: not x),
        ops.do_action(lambda x: print(f"trigger_stop")),
        ops.share()
    )

    countdown = trigger_start.pipe(
        ops.flat_map(
            lambda _: create_countdown(timer, 10).pipe(
                ops.take_until(trigger_stop)
            )
        ),
    )
    trigger_start.pipe(
        ops.flat_map(
            lambda _: rx.interval((10 - 2) / 1000).pipe(
                ops.take_until(trigger_stop)
            )
        ),
    ).subscribe(
        lambda i: update_ui(ui.progress_ring, i / 1000)
    )
    countdown.pipe(
        ops.filter(lambda t: t < 0),
        # ops.delay(1),
    ).subscribe(
        lambda i: subprocess.call(["afplay", "/System/Library/Sounds/Glass.aiff"])
    )
    state.pipe(
        ops.map(lambda s: 'water' in s),
    ).subscribe(lambda f: update_ui(ui.countdown.parent, f, property='visible'))
    state.subscribe(
        lambda t: update_ui(ui.image, state2filename(t), property='src')
    )
    weight.subscribe(
        lambda w: update_ui(ui.weight_button, f"{w:.1f} гр.", property='text')
    )
    trigger_stop.subscribe(
        lambda w: update_ui(ui.progress_ring, 0)
    )
    countdown.subscribe(
        lambda t: update_ui(ui.countdown, format_seconds(t))
    )
    timer.subscribe(lambda x: print(f"session_timer: {x}"))

    rx.combine_latest(timer, state, weight).subscribe(
        on_next=lambda v: update_ui(ui.statistics_details.title, format_statistics(v))
    )
    timer.connect()
    weight.connect()


if __name__ == '__main__':
    print(rx.__version__)
    ft.app(target=main, assets_dir='assets')
