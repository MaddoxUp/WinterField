# -*- coding:utf-8-*-
# Copyright (C) 2021-2022 THCWorkshopCN
"""
工具箱
"""
from . import global_values as gv

def get_type(variate:any) -> str:
    """判断值的类型"""
    type=None
    if isinstance(variate,int): type = "int"
    elif isinstance(variate,str): type = "str"
    elif isinstance(variate,float): type = "float"
    elif isinstance(variate,list): type = "list"
    elif isinstance(variate,tuple): type = "tuple"
    elif isinstance(variate,dict): type = "dict"
    elif isinstance(variate,set): type = "set"
    return type

@property
def CENTER():
    """自动获取屏幕中央的位子，但是似乎会与d_ratio缩放冲突。添加了@property修饰，无需实例化。"""
    screen_width, screen_height = gv.get("screen_size")
    CENTER = (screen_width/2, screen_height/2)
    return CENTER