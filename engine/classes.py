# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""类的定义"""
from . import basic_gui


class TextSurface(object):
    pass


class EventGetter(object):
    """需要获取Event的类"""
    def __init__(self, get_expected_events=False) -> None:
        self.expected_events: list = []

    def receive_event(self, event):
        pass
