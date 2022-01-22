# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""程序启动模块"""

from app.locals import REAL_HEIGHT, REAL_WIDTH
from app.modules import classes, events
from app.modules import global_values as gv
import pygame
from pygame.locals import *
from app.modules import events
from app import basic_display
from app import integrated_display_functions as display

def startup() -> None:
    """启动程序"""
    global screen_size, screen, screen_width, screen_height, isfullscreen
    screen = gv.get("screen")
    screen_size = gv.get("screen_size")
    screen_width = gv.get("screen_width")
    screen_height = gv.get("screen_height")
    events.program_start().announce()
    fps = gv.get("fps")
    fps.tick(3)
    isfullscreen = False
    gv.set("isfullscreen",isfullscreen)
    pygame.display.set_caption("One Billions")
    basic_display.renderer().fill((104,204,255))
    display.render_text("十亿分之一",0,80,location=(REAL_WIDTH/2,REAL_HEIGHT/2),location_type="middle",background_color=(0,0,0))
    #UNFINISHED