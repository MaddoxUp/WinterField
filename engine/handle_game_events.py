# -*- coding:utf-8-*
# Copyright (C) 2021-2022 THCWorkshopCN
from . import classes
import pygame


class EventRegistry(object):
    def __init__(self) -> None:
        super(EventRegistry, self).__init__()

    def init(self) -> None:
        global registered_events
        registered_events = {}
        scs = classes.EventGetter.__subclasses__()
        for sc in scs:
            print(scs)
            processing_class = sc
            if sc.__name__ not in ["Button"]:
                for i in range(len(processing_class.expected_events)):
                    try:
                        _list = registered_events[str(processing_class.expected_events[i])]
                    except KeyError:
                        _list = []
                        registered_events[str(processing_class.expected_events[i])] = []
                    finally:
                        _list.append(sc)
                        registered_events[str(processing_class.expected_events[i])] = _list
                        print(registered_events)

    def handle_events(self, events) -> None:
        for event in events:
            for i in list(registered_events.keys()):
                print("here")
                if event.type == int(i) and event.type != pygame.constants.MOUSEBUTTONDOWN:
                    print("notgood")
                    for j in registered_events[i]:
                        j().receive_event(event)
                elif event.type == pygame.constants.MOUSEBUTTONDOWN:
                    print("triggered")
                    for clicked_object in registered_events[str(pygame.constants.MOUSEBUTTONDOWN)]:
                        print(clicked_object)
                        if clicked_object.surface.rect.collidepoint(event.pos):
                            print("clicked")
                            clicked_object().clicked()
#TODO： 实现按钮被点击时执行函数的效果
