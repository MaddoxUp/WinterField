# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""程序主体"""

from . import basic_display
from .modules import global_values as gv
gv._init()
basic_display._init()

def _init():
    """开始加载模块"""
    basic_display._init() #初始化显示模块