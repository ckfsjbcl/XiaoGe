"""
used to create a light command
"""
import os

import tools

__version__ = 1.0


def get_files_name(path):
    return os.listdir(path)


class LightCommand:
    def __init__(self, name='LightCommand'):
        # 初始化
        if 'START.txt' not in get_files_name('.'):
            with open('START.txt', 'r+') as Startfile:
                Startfile.write(f'* Create Time: {tools.get_time_now__()}\n'
                                f'* Version: {__version__}\n'
                                f'* Name: {name}\n'
                                f'!本文件为启动必须,若删除则会覆盖所有已配置参数,若需重置则删除本文件即可!\n')
                print("控制台配置文件重载中...")


class FILES:
    def __init__(self):
        ...

    def __get__(self, instance, owner):
        ...


Command = LightCommand()
