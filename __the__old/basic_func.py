"""
储存一些基础函数
"""
import importlib
import json
import time



def get_time_now__():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def implement__(post: str, location):
    # post用于上报指令或消息，location是上报位置
    try:
        model = importlib.import_module(location)
        return model.take_in(post)
    except:
        """"""
        # TODO error


def colorful_out__(msg: str, func: callable, color_f=False, color_b=False, color_mod=0):
    """
    暂时不支持默认模式,我也不知道bug出自哪里
    mod: 
        0->默认
        1->高亮(加粗)
        4->下划线
        7->反显
        8->全行打印背景色
    """
    match_dict_f = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "plum": 35,
        "cyan": 36,
        "white": 37
    }
    match_dict_b = {
        "black": 40,
        "red": 41,
        "green": 42,
        "yellow": 43,
        "blue": 44,
        "plum": 45,
        "cyan": 46,
        "white": 47
    }
    try:
        color_f, color_b = match_dict_f[color_f], match_dict_b[color_b]
    except:
        if not color_b and not color_f:
            print("颜色输入错误,超出范围")
    msg_mod=str(color_mod)+';'
    msg_f=''
    msg_b=''
    if not color_mod==8:
        msg_1=r'\033[0m'
    if  color_f is not None:
        msg_f=str(color_f)+';'
    if  color_b is not None:
        msg_b=str(color_b)+';'
    out_msg=msg_mod+msg_f+msg_b+"m"+msg
    re_msg=func(f'\033[{color_mod};{color_f};{color_b}m{msg}\033[0m')
    #re_msg=func(f"\033[{out_msg}\033[0m")
    #默认打印模式(上一行)暂有bug,请勿去掉注释
    return re_msg
    
    


def load_json__(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


def match_num__(key: str, msg: str) -> list:
    if key in msg:
        for i in range(len(msg)):
            if key == msg[i:i + len(key)]:
                return [i, i + len(key)]
    else:
        ...
        # TODO error

