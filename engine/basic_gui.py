# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""提供基础的用户界面"""
from . import basic_display
from . import integrated_display_functions as idf


class Button(object):
    """新建按钮。通过传入registered_function参数来指定点击后的效果"""

    def __init__(self, text: str, color: tuple, registered_function=None, size: int = 5, direct_render: bool = False,
                 location: tuple = (0, 0), layer: int = 0):
        self.surface = idf.render_text(text, 0, size, (0, 0), color, direct_render=False)[0]
        self.location = location
        self.layer = layer
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()
        self.registered_function = registered_function
        if direct_render:
            basic_display.renderer().addobject(self.surface, location, layer, self)

    def clicked(self, position):
        """判断自身是否被点中"""
        x_match = self.location[0] < position[0] < self.x + self.WIDTH
        y_match = self.location[1] < position[1] < self.y + self.HEIGHT
        if x_match and y_match:
            return True
        else:
            return False

    @property
    def return_object(self):
        """返回自身用于basic_display.renderer.add_object的相关参数"""
        return self.surface, self.location, self.layer, self
