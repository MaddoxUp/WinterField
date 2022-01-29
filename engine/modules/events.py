# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN

"""
Event体系主模块
"""
def init() -> None:
    global gv
    from . import global_values as gv
    global get_type
    from .tools import get_type
    global time
    import time
    gv.set("ex-notify",None)
    gv.set("notify",None)

class events(object):
    """events根类，请勿调用"""
    def __init__(self) -> None:
        super().__init__()
        self.event_name = "events"
    def announce(self) -> None:
        gv.set("ex-notify",gv.get("notify"))
        gv.set("notify",self.event_name)

class program_start(events):
    """程序开始运行的event"""
    def __init__(self) -> None:
        super().__init__()
        self.event_name = self.event_name + "."
        self.event_name = self.event_name + "program_start"

#有关于画面的event
class display(events):
    """有关于画面的event"""
    def __init__(self) -> None:
        super().__init__()
        self.event_name = self.event_name + "."
        self.event_name = self.event_name + "display"
class window_resized(display):
    """窗口大小重设"""
    def __init__(self) -> None:
        super().__init__()
        self.event_name = self.event_name + "."
        self.event_name = self.event_name + "window_resized"
