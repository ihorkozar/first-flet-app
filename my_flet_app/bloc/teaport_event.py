from bloc.teapot_state import TeapotStatus


class AppEvent:
    pass

class StartTimer(AppEvent):
    pass

class StartStreamEvent(AppEvent):
    pass

class UpdateIterationTimeEvent(AppEvent):
    def __init__(self, iteration_time: int):
        self.iteration_time = iteration_time

class UpdateCountEvent(AppEvent):
    def __init__(self, count: int):
        self.count = count

class UpdateStatusEvent(AppEvent):
    def __init__(self, teapot_status: TeapotStatus):
        self.teapot_status = teapot_status


class UpdateWeightEvent(AppEvent):
    def __init__(self, weight: int):
        self.weight = weight
