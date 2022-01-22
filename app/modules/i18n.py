# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
"""多语言系统"""
import i18n
import locale

i18n.load_path.append("./translations/terminal_output")
i18n.load_path.append("./translations")
i18n.set('available_locales',["en","zh_CN","zh_TW"])
i18n.set("locale",locale.getdefaultlocale()[0])

def trans(content:str):
    """将内容翻译为对应用户语言"""
    return i18n.t(content)