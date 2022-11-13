"""
class基类
"""
import basic_func

"""
基类都为__xxx__
"""


class __event__:
    """事件基类"""

    def __init__(self):
        # ---------------
        self.tag = __tag__()
        # ---------------
        self.to_func = None


class __post__:
    """通讯消息基类"""

    def __init__(self):
        # ---------------
        self.tag = __tag__()
        # ---------------


class __get__:
    """通讯消息基类"""

    def __init__(self):
        # ---------------
        self.tag = __tag__()
        # ---------------


class __msg__:
    """消息基类"""

    def __init__(self):
        # ---------------
        self.tag = __tag__()
        # ---------------


class __error__:
    """报错基类"""

    def __init__(self):
        # ---------------
        self.tag = __tag__()
        # ---------------

    def error_match(self, name: str):
        ...


class __tag__:
    """tag基类"""

    def __init__(self, time=basic_func.get_time_now__()):
        self.tag_pool = {
            "head": "tag"
        }
        self.add_tag("time", time)

    def add_tag(self, key, value):
        self.tag_pool[key] = value


class __main__:
    def __init__(self):
        # ---------------
        self.tag = __tag__()
        # ---------------
        self.main_loop = []

    def add_loop(self, post, mod=0, index=0):

        if isinstance(post, str):
            post = [post]

        if mod == 0:
            # 基础模式,将最新上报传输至loop尾部
            self.main_loop = self.main_loop + post
        elif mod == 1:
            # 将最新上报传输至loop顶部
            self.main_loop = post + self.main_loop
        elif mod == 2:
            # 将最新上报添加的指定部位之前
            for i in reversed(post):
                self.main_loop = self.main_loop.insert(index, i)
        else:
            ...
            # TODO error

    def del_loop(self, post, mod=0):
        # mod 0 删除第一个特定值
        if mod == 0:
            self.main_loop.remove(post)
        # mod 1 删除所有特定值
        elif mod == 1:
            for i in range(len(self.main_loop)):
                try:
                    self.main_loop.remove(post)
                except:
                    pass
        # mod 2 删除指定位置的值
        elif mod == 2:
            if isinstance(post, int):
                del self.main_loop[post]
            elif isinstance(post, list):
                if len(post) == 2:
                    del self.main_loop[post[0]:post[1]]
                else:
                    ...
                    # TODO error

    def post(self, *args):
        for i in args:
            self.add_loop(i)


class __null__:
    """未知基类"""


class __command__:
    """控制台"""

    def __init__(self, path: str, name: str):
        self.json_path,self.json_name = path,name
        self.data = basic_func.load_json__(path)[name]

    def match(self, input_msg: str):
        # TODO 匹配
        # input_msg = xxx(前缀) -start botname=bot mod=1
        #          or xxx      -start bot 1
        for keys in self.data:
            """
            if keys in input_msg:
                num = basic_func.match_num__(keys, input_msg)
                if input_msg[num[0]-1] == '-':
                    value = self.data[keys]
            """
            keys = '-' + keys
            if keys in input_msg:
                input_list = input_msg.split()
                match_list = []
                re_dict = {}
                for dicts in self.data[keys]:
                    if dicts[0] == '--help':
                        ...
                    elif dicts[0][0:6] == 'input_':
                        left_msg = dicts[0][6:]
                        match_list.append(left_msg)
                if len(match_list) != len(input_list):
                    ...
                    # TODO error
                for i in range(len(match_list)):
                    re_dict[match_list[i]] = input_list[i]
                    return re_dict

    def __main__(self,do):
        if do is True:
            ...
        else:
            self.__init__(path=self.json_path,name=self.json_name)
            #只刷新不操作
            #此功能暂时废除
        #主控

class bot:
    def __init__(self):
        self.pool =[]