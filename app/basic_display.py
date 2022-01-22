# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""基础的显示模块"""

from .modules import classes
from .modules import global_values as gv
import pygame
from pygame.locals import *
import tkinter
import operator
from app.locals import *
import PIL
from io import StringIO
from PIL import Image

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
    calculate_d_ratio()

def calculate_d_ratio() -> classes.display.display_map:
    """重新计算显示大小与真实大小的比值，用于缩放"""
    global d_width_ratio, d_height_ratio, d_ratio, screen_width, screen_height, screen_size
    screen_width, screen_height = screen_size
    d_width_ratio = screen_width/REAL_WIDTH
    d_height_ratio = screen_height/REAL_HEIGHT
    d_ratio = (d_width_ratio, d_height_ratio)
    gv.set("d_ratio",d_ratio)
    gv.set("d_width_ratio",d_width_ratio)
    gv.set("d_height_ratio",d_height_ratio)
    print((d_width_ratio,d_height_ratio))

class renderer(object):
    """与画面呈现直接有关的函数"""
    def __init__(self) -> None:
        global _fill, object_list, d_ratio
    def addobject(self,_source:pygame.Surface,location:tuple,layer:int=0,name:str=None) -> classes.display.display_map:
        """往渲染列表中添加object"""
        args = {"_source":_source,"location":location,"layer":layer,"d_ratio":d_ratio,"name":name,"initial_source":_source,"initial_location":location}
        object_list.append(args)
    def fill(self,color:tuple):
        global fill_color
        fill_color = color
    def smart_render(self) ->classes.display:
        """自动检测画面中需要渲染的部分并进行渲染"""
        pass
    def rerender(self) -> classes.display:
        """对画面进行彻底的重新渲染"""
        #将列表按优先级进行排列，实现图层覆盖
        object_list = objl_sort()
        screen.fill(fill_color)
        for i in range(len(object_list)):
            if object_list[i]["d_ratio"] != d_ratio: #判断元素在渲染前是否需要缩放与位置更改
                initial_source = object_list[i]["initial_source"]
                rect = initial_source.get_rect()
                new_size = rect.width*d_width_ratio, rect.height*d_height_ratio
                object_list[i]["_source"] = pygame.transform.scale(initial_source,new_size)
                my_location = object_list[i]["initial_location"]
                object_list[i]["location"] = my_location[0]*d_width_ratio, my_location[1]*d_height_ratio
                object_list[i]["d_ratio"] = d_ratio
            screen.blit(object_list[i]["_source"],object_list[i]["location"])

def resize(isfullscreen) -> classes.display:
    resized = False
    global screen_size, screen_width, screen_height, object_list, d_width_ratio, d_height_ratio, d_ratio
    # 这个函数中必须先判断窗口大小是否变化，再判断是否全屏
    # 否则，在全屏之后，pygame会判定为全屏操作也是改变窗体大小的一个操作，所以会显示一个比较大的窗口但不是全屏模式
    for event in pygame.event.get(VIDEORESIZE):
        backup_screen_size = screen_size
        screen_size = screen_width, screen_height = event.size
        gv.set("backup_screen_size",screen_size)
        screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
        calculate_d_ratio()
        gv.set("screen",screen)
        resized = True
    for event in pygame.event.get(KEYDOWN):
        if event.key == K_F11:
            if not isfullscreen:
                isfullscreen = True
                backup_screen_size = screen_size
                gv.set("backup_screen_size",backup_screen_size)
                screen_size = screen_width, screen_height =  (tk.winfo_screenwidth(),tk.winfo_screenheight())
                screen = pygame.display.set_mode(screen_size, FULLSCREEN|HWSURFACE|DOUBLEBUF)
                calculate_d_ratio()
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
        renderer().rerender()
    return isfullscreen