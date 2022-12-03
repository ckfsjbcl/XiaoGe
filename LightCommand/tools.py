"""
用来储存一些基本函数
"""
import json
import time

import yaml


def print_log(msg, mod):
    with open('Cache/log.txt', 'a+') as log:
        log.write(
            f"[{get_time_now__()}]:|{mod}|#{msg}#"
        )


def get_time_now__():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def load_json__(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


def load_yaml__(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.load(f.read())
