# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN

from .modules import events,classes
from .modules import global_values as gv
import pygame
from pygame.locals import *
from .modules import events
from . import basic_display
from .locals import *

def render_text(
    _text:str, layer:int=0, size:int=50, location:tuple=(0,0), color=(255,255,255), location_type:str = "middle", sysfont:str = None, font:str=None, _antialias:bool=True,background_color:tuple = None,
    ) -> classes.display.display_map:
    """渲染文字"""
    screen = gv.get("screen")
    background = gv.get("background")
    if sysfont is not None:
        text = pygame.font.SysFont(sysfont,size)
    else:
        if font is not None:
            text = pygame.font.Font(font,size)
        else:
            text = pygame.font.Font("./fonts/SourceHanSans-Light.otf",size)
    text_img = text.render(_text,_antialias,color,background_color)
    if location_type == "middle":
        text_fmt_rect = text_img.get_rect()
        location_x, location_y = location
        location_x -= text_fmt_rect.width/2
        location_y -= text_fmt_rect.height/2
        location = (location_x,location_y)
    basic_display.renderer().addobject(text_img,location,layer,"text_img")