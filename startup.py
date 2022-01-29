# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""程序启动模块"""

import pygame
import engine
from engine import basic_gui
from engine.locals import REAL_HEIGHT, REAL_WIDTH
from engine.modules import global_values as gv
from engine import integrated_display_functions as idf

def startup() -> None:
    """启动程序"""
    engine.events.program_start().announce()
    fps = gv.get("fps")
    fps.tick(3)
    isfullscreen = False
    gv.set("isfullscreen",isfullscreen)
    pygame.display.set_caption("One Billions")
    engine.basic_display.renderer().fill((104,204,255))
    idf.render_text("十亿分之一",0,80,location=(REAL_WIDTH/2,REAL_HEIGHT/2),location_type="middle",background_color=(0,0,0))
    start_button = basic_gui.button("开始",(0,0,0),lambda:print("clicked"),direct_render=True,layer=1)
    #UNFINISHED