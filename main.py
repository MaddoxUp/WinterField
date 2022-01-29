# -*- coding:utf-8-*-
# Copyright (C) 2021-2022 THCWorkshopCN
"""程序入口"""
import sys

sys.dont_write_bytecode = True
from engine.modules import i18n

print(i18n.trans("output.loading_libraries"))

# Pygame
import pygame
from pygame.locals import *

pygame.init()

print(i18n.trans("output.loading_modules"))

import engine

print(i18n.trans("output.loading_classes"))

# Main program
import startup


def main():  # 主程序过程
    engine.init()
    engine.locals.default_font_path = "./fonts/SourceHanSans-Light.otf"
    startup.startup()
    is_full_screen = None
    fps = pygame.time.Clock()
    while True:  # 主循环
        is_full_screen = engine.basic_display.resize(is_full_screen)  # 判断窗口大小是否改变
        events = pygame.event.get()
        for event in events:  # 循环开始
            if event.type == QUIT:  # 退出事件
                pygame.quit()
                sys.exit()
        engine.handle_game_events.EventRegistry().handle_events(events)
        engine.basic_display.Renderer().re_render()
        pygame.display.flip()  # 更新画面
        fps.tick(3)


if __name__ == "__main__":
    main()
