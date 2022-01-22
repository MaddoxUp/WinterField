# -*- coding:utf-8-*-
# Copyright (C) 2021-2022 THCWorkshopCN
"""程序入口"""
import sys
sys.dont_write_bytecode = True
from app.modules import i18n

print(i18n.trans("output.loading_libraries"))

#Threading
import threading
#Pygame
import pygame
from pygame.constants import *
from pygame.locals import *
pygame.init()

print(i18n.trans("output.loading_modules"))

from app.modules import events, global_values as gv
gv._init()
from app.modules import tools
from app.modules import events
events._init()

print(i18n.trans("output.loading_classes"))

#Class definations
from app.modules import classes
#Main program
import app
import startup
app._init()
def main(): #主程序过程
    global app,isfullscreen
    app._init()
    startup.startup()
    isfullscreen = None
    while True:  #主循环
        isfullscreen = app.basic_display.resize(isfullscreen) #判断窗口大小是否改变
        for event in pygame.event.get(): #循环开始
            if event.type == QUIT: #退出事件
                pygame.quit()
                sys.exit()
        #循环末尾
        app.basic_display.renderer().rerender()
        pygame.display.flip() #更新画面

if __name__ == "__main__":
    main()