# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""程序启动模块"""

from engine.locals import REAL_HEIGHT, REAL_WIDTH
from engine.modules import events
from engine.modules import global_values as gv
import pygame
from pygame.locals import *
from engine.modules import events
from engine import basic_display
from engine import integrated_display_functions as display

def startup() -> None:
    """启动程序"""
    events.program_start().announce()
    fps = gv.get("fps")
    fps.tick(3)
    isfullscreen = False
    gv.set("isfullscreen",isfullscreen)
    pygame.display.set_caption("One Billions")
    basic_display.renderer().fill((104,204,255))
    display.render_text("十亿分之一",0,80,location=(REAL_WIDTH/2,REAL_HEIGHT/2),location_type="middle",background_color=(0,0,0))
    #UNFINISHED