# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""提供基础的用户界面"""
import types
import pygame.constants
from . import basic_display
from . import integrated_display_functions as idf
from . import classes


class Button(classes.EventGetter):
    """新建按钮。通过传入registered_function参数来指定点击后的效果"""

    def __init__(self, text: str = None, color: tuple = None, registered_function=None, size: int = 5,
                 direct_render: bool = False, location: tuple = (0, 0), layer: int = 0,
                 get_expected_events: bool = False):
        super(Button, self).__init__()
        self.expected_events.append(pygame.constants.MOUSEBUTTONDOWN)
        if not get_expected_events:
            self.surface = idf.render_text(text, 0, size, (0, 0), color, direct_render=False)[0]
            self.location = location
            self.layer = layer
            self.WIDTH = self.surface.get_width()
            self.HEIGHT = self.surface.get_height()
            self.SIZE = self.WIDTH, self.HEIGHT
            self.registered_function = registered_function
            self.d_location = self.location
            self.d_size = self.SIZE
            if direct_render:
                basic_display.Renderer().add_object(self.surface, location, layer, self)

    def __call__(self, get_expected_events: bool = False,):
        return self.expected_events

    def receive_event(self, event):
        if event.type == pygame.constants.MOUSEBUTTONDOWN:
            self.check_clicked()

    def clicked(self):
        """判断自身是否被点中，若被点中则执行registered_function"""

        todo = None
        if isinstance(type(self.registered_function), dict):
            todo = self.registered_function[str(pygame.constants.MOUSEBUTTONDOWN)]
        if isinstance(type(self.registered_function), list) or isinstance(type(todo), list):
            for function_doing in todo:
                function_doing()
        elif isinstance(type(self.registered_function), types.FunctionType):
            self.registered_function()
        else:
            raise TypeError('The value of "registered_function" for a "Button" should be a function or a list of '
                            'functions or a dict which has key "str(pygame.constants.MOUSEBUTTONDOWN)" and its value '
                            'is what I said just now.')

    @property
    def return_object_list_friendly_attrs(self):
        """返回自身用于basic_display.renderer.add_object的相关参数"""
        return self.surface, self.location, self.layer, self
