# -*- coding:utf-8-*-
# Copyright (C) 2021-2022 THCWorkshopCN
"""程序入口"""
import sys
sys.dont_write_bytecode = True
from engine.modules import i18n

print(i18n.trans("output.loading_libraries"))

#Pygame
import pygame
from pygame.constants import *
from pygame.locals import *
pygame.init()

print(i18n.trans("output.loading_modules"))

from engine.modules import events, global_values as gv
gv._init()
from engine.modules import tools
from engine.modules import events
events._init()

print(i18n.trans("output.loading_classes"))

from engine.modules import classes
#Main program
import engine
import startup
engine._init()
def main(): #主程序过程
    global engine,isfullscreen
    engine._init()
    startup.startup()
    isfullscreen = None
    while True:  #主循环
        isfullscreen = engine.basic_display.resize(isfullscreen) #判断窗口大小是否改变
        for event in pygame.event.get(): #循环开始
            if event.type == QUIT: #退出事件
                pygame.quit()
                sys.exit()
        engine.basic_display.renderer().rerender()
        pygame.display.flip() #更新画面

if __name__ == "__main__":
    main()