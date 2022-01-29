# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""
WinterField，一个简单易懂的自制2D游戏引擎 by THCWorkshopCN\n
支持的功能并不多，但如果你想绕开基层的开发快速实现你的想法，那么这个开箱即用引擎将是不错的选择。\n
本引擎基于pygame开发，Python版本3.8.10\n
支持的操作系统：\n
Windows(7以及更高版本), Linux, MacOS, OS X, FreeBSD, IRIX, BeOS
"""

from . import basic_display
from .modules import global_values as gv
from .modules import events
from . import basic_gui
gv._init()
basic_display._init()



def _init():
    """开始加载模块"""
    events._init()
    basic_display._init() #初始化显示模块