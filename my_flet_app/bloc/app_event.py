class AppEvent:
    pass

class UpdateCurrentTimeEvent(AppEvent):
    def __init__(self, current_time: int):
        self.current_time = current_time

class UpdateFullTimeEvent(AppEvent):
    def __init__(self, full_time: int):
        self.full_time = full_time

class UpdateIterationTimeEvent(AppEvent):
    def __init__(self, iteration_time: int):
        self.iteration_time = iteration_time

class UpdateCountEvent(AppEvent):
    def __init__(self, count: int):
        self.count = count