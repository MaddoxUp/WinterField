# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""基础的显示模块"""
from .modules import global_values as gv
import pygame
from pygame.locals import *
import tkinter
import operator
from engine.locals import *


def object_list_sort() -> list:
    global object_list
    return sorted(object_list, key=operator.itemgetter("layer"))


tk = tkinter.Tk()


def init() -> None:
    """初始化display模块"""
    global screen, screen_size, screen_width, screen_height, background
    screen_size = screen_width, screen_height = 800, 600
    global fps
    fps = pygame.time.Clock()
    gv.set("fps", fps)
    screen = pygame.display.set_mode(screen_size, DOUBLEBUF | RESIZABLE)
    background = pygame.Surface(screen.get_size())
    gv.set("screen", screen)
    gv.set("screen_size", screen_size)
    gv.set("screen_width", screen_width)
    gv.set("screen_height", screen_height)
    gv.set("background", background)
    global object_list
    object_list = []
    global backup_screen_size
    backup_screen_size = screen_size
    gv.set("backup_screen_size", backup_screen_size)
    calculate_d_ratio()


def transforming(_object_list):
    for i in range(len(_object_list)):
        if _object_list[i]["d_ratio"] != d_ratio:  # 判断元素在渲染前是否需要缩放与位置更改
            initial_source = _object_list[i]["initial_source"]
            rect = initial_source.get_rect()
            new_size = rect.width * d_width_ratio, rect.height * d_height_ratio
            new_source = pygame.transform.scale(initial_source, new_size)
            _object_list[i]["_source"] = new_source
            my_location = _object_list[i]["initial_location"]
            new_location = my_location[0] * d_width_ratio, my_location[1] * d_height_ratio
            _object_list[i]["location"] = new_location
            _object_list[i]["d_ratio"] = d_ratio
            _object_list[i]["d_size"] = (new_source.get_width(), new_source.get_height())
            try:
                _object_list[i]["from"].d_location = new_location
            except AttributeError:
                pass
    return _object_list


def calculate_d_ratio() -> None:
    """重新计算显示大小与真实大小的比值，用于缩放"""
    global d_width_ratio, d_height_ratio, d_ratio, screen_width, screen_height, screen_size
    screen_width, screen_height = screen_size
    d_width_ratio = screen_width / REAL_WIDTH
    d_height_ratio = screen_height / REAL_HEIGHT
    d_ratio = (d_width_ratio, d_height_ratio)
    gv.set("d_ratio", d_ratio)
    gv.set("d_width_ratio", d_width_ratio)
    gv.set("d_height_ratio", d_height_ratio)


class Renderer(object):
    """与画面呈现直接有关的函数"""

    def __init__(self) -> None:
        self.ex_object_list = None
        global _fill, object_list, d_ratio

    @staticmethod
    def add_object(_source: pygame.Surface, location: tuple, layer: int = 0, _from: object = None) -> None:
        """往渲染列表中添加object"""
        args = {
            "_source": _source,
            "location": location, "layer": layer,
            "d_ratio": d_ratio, "d_size": (_source.get_width(), _source.get_height),
            "initial_source": _source, "initial_location": location,
            "from": _from
        }
        object_list.append(args)

    @staticmethod
    def fill(color: tuple):
        global fill_color
        fill_color = color

    def smart_render(self) -> None:
        """自动检测画面中需要渲染的部分并进行渲染，由于设计不是很聪明，不一定能提升性能。目前还未完成。"""
        global object_list
        smart_render_list = []
        object_list = object_list_sort()
        self.ex_object_list = object_list
        if self.ex_object_list != object_list:
            for i in range(len(self.ex_object_list)):
                if self.ex_object_list[i] != object_list[i]:
                    smart_render_list.append(object_list[i])
                if len(object_list) > len(self.ex_object_list):
                    pass

    def re_render(self) -> None:
        """对画面进行彻底的重新渲染"""
        global object_list
        # 将列表按优先级进行排列，实现图层覆盖
        object_list = object_list_sort()
        self.ex_object_list = object_list
        screen.fill(fill_color)
        object_list = transforming(object_list)
        for i in range(len(object_list)):
            screen.blit(object_list[i]["_source"], object_list[i]["location"])


def resize(is_full_screen) -> bool:
    resized = False
    global screen_size, screen_width, screen_height, object_list, d_width_ratio, d_height_ratio, d_ratio
    global backup_screen_size, screen
    # 这个函数中必须先判断窗口大小是否变化，再判断是否全屏
    # 否则，在全屏之后，pygame会判定为全屏操作也是改变窗体大小的一个操作，所以会显示一个比较大的窗口但不是全屏模式
    for event in pygame.event.get(VIDEORESIZE):
        backup_screen_size = screen_size
        screen_size = screen_width, screen_height = event.size
        gv.set("backup_screen_size", screen_size)
        screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
        calculate_d_ratio()
        gv.set("screen", screen)
        resized = True
    for event in pygame.event.get(KEYDOWN):
        if event.key == K_F11:
            if not is_full_screen:
                is_full_screen = True
                backup_screen_size = screen_size
                gv.set("backup_screen_size", backup_screen_size)
                screen_size = screen_width, screen_height = (tk.winfo_screenwidth(), tk.winfo_screenheight())
                screen = pygame.display.set_mode(screen_size, FULLSCREEN | HWSURFACE | DOUBLEBUF)
                calculate_d_ratio()
                gv.set("screen", screen)
                resized = True
            else:
                is_full_screen = False
                backup_screen_size = gv.get("backup_screen_size")
                screen_size = screen_width, screen_height = backup_screen_size
                calculate_d_ratio()
                screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | RESIZABLE)
                gv.set("screen", screen)
                resized = True
            pygame.event.post(event)
            # BUG :按F11进入全屏并取消全屏后，尽管重新声明了RESIZABLE，但无法再改变窗口大小
    if resized:
        Renderer().re_render()
    return is_full_screen
