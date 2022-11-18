"""
used to create a light command
"""
import os

import tools

__version__ = 1.0


class LightCommand:
    def __init__(self, name='LightCommand'):
        # 初始化
        if 'START.txt' not in self.get_files_name('.'):
            with open('START.txt', 'r+') as Startfile:
                Startfile.write(f'Create Time:{tools.get_time_now__()}\n'
                                f'Version:{__version__}'
                                f'Name:{name}')

    def get_files_name(self, path):
        return os.listdir(path)


Command = LightCommand()
