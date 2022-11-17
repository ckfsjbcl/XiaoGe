"""
用来储存一些基本函数
"""
import time


def print_log(msg, mod):
    with open('Cache/log.txt', 'a+') as log:
        log.write(
            f"[{get_time_now__()}]:/{mod}/#{msg}#"
        )


def get_time_now__():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
