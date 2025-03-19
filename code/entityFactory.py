#!/usr/bin/python
# -*- coding: utf-8 -*-
from Const import WIN_WIDTH
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1L':
                list_l = []
                for i in range(4):
                    list_l.append(Background(f'Level1L{i}', (0, 0)))
                    list_l.append(Background(f'Level1L{i}', (WIN_WIDTH, 0)))
                return list_l
