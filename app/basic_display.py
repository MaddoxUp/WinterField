# -*- coding:utf-8-*
# Copyright (C) 2021 THCWorkshopCN
"""基础的显示模块"""

from modules import classes,events
from modules import global_values as gv
import pygame
from pygame.locals import *
import tkinter
import numpy as np
from numba import jit
import operator
from app.locals import *

@jit
def objl_sort():
    global object_list
    return sorted(object_list, key=operator.itemgetter("layer"))

tk = tkinter.Tk()
def _init():
    """初始化display模块"""
    global screen,screen_size,screen_width,screen_height,background
    screen_size = screen_width, screen_height = 800,600
    global fps
    fps = pygame.time.Clock()
    gv.set("fps",fps)
    fps.tick(60)
    screen = pygame.display.set_mode(screen_size,DOUBLEBUF|RESIZABLE)
    background = pygame.Surface(screen.get_size())
    gv.set("screen",screen)
    gv.set("screen_size",screen_size)
    gv.set("screen_width",screen_width)
    gv.set("screen_height",screen_height)
    gv.set("background",background)
    global object_list
    object_list = []
    global backup_screen_size
    backup_screen_size = screen_size
    gv.set("backup_screen_size",backup_screen_size)

def calculate_d_ratio() -> classes.display.display_map:
    """重新计算显示大小与真实大小的比值，用于缩放"""
    global d_width_ratio, d_height_ratio, d_ratio
    d_width_ratio = screen_width/REAL_WIDTH
    d_height_ratio = screen_height/REAL_HEIGHT
    d_ratio = (d_width_ratio, d_height_ratio)
    gv.set("d_ratio",d_ratio)
    gv.set("d_width_ratio",d_width_ratio)
    gv.set("d_height_ratio",d_height_ratio)

class renderer(object):
    """与画面呈现直接有关的函数"""
    def __init__(self) -> None:
        global _fill
        global object_list
    def addobject(self,_source,location,layer:int=0,name = None) -> classes.display.display_map:
        """往渲染列表中添加object"""
        args = {"_source":_source,"location":location,"layer":layer,"d_ratio":d_ratio,"name":name}
        object_list.append(args)
    def fill(self,color:tuple):
        global _fill_R, _fill_G, _fill_B
        _fill_R, _fill_G, _fill_B = color
    def render(self) -> classes.display:
        """渲染画面"""
        #将列表按优先级进行排列，实现图层覆盖
        object_list = objl_sort()
        screen.fill((_fill_R,_fill_G,_fill_B))
        for i in range(len(object_list)):
            if object_list[i]["d_ratio"] != d_ratio: #判断元素在渲染前是否需要缩放与位置更改
                pass #UNFINISHED
            screen.blit(object_list[i]["_source"],object_list[i]["location"])
    class event_handler(object):
        pass

def resize(isfullscreen) -> classes.display:
    resized = False
    global screen_size, object_list, d_width_ratio, d_height_ratio, d_ratio
    # 这个函数中必须先判断窗口大小是否变化，再判断是否全屏
    # 否则，在全屏之后，pygame会判定为全屏操作也是改变窗体大小的一个操作，所以会显示一个比较大的窗口但不是全屏模式
    for event in pygame.event.get(VIDEORESIZE):
        backup_screen_size = screen_size
        screen_size = screen_width, screen_height = event.size
        calculate_d_ratio()
        gv.set("backup_screen_size",screen_size)
        screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
        gv.set("screen",screen)
        resized = True
    for event in pygame.event.get(KEYDOWN):
        if event.key == K_F11:
            if not isfullscreen:
                isfullscreen = True
                backup_screen_size = screen_size
                gv.set("backup_screen_size",backup_screen_size)
                screen_size = screen_width, screen_height =  (tk.winfo_screenwidth(),tk.winfo_screenheight())
                display_info = pygame.display.Info()
                calculate_d_ratio()
                screen = pygame.display.set_mode(screen_size, FULLSCREEN|HWSURFACE|DOUBLEBUF)
                gv.set("screen",screen)
                resized = True
            else:
                isfullscreen = False
                backup_screen_size = gv.get("backup_screen_size")
                screen_size = screen_width, screen_height = backup_screen_size
                calculate_d_ratio()
                screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|RESIZABLE)
                gv.set("screen",screen)
                resized = True
            pygame.event.post(event)
            #BUG :按F11进入全屏并取消全屏后，尽管重新声明了RESIZABLE，但无法再改变窗口大小
    if resized:
        renderer.render()
    return isfullscreen