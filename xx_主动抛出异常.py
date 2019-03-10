def password():
    pwd = input('请输入密码：')
    if len(pwd) < 8:
        #两种创建异常的方式
        raise Exception('密码长度不足8位')
        # ex=Exception('密码长度不足')
        # raise ex
    return pwd


try:
    print(password())
except Exception as result:
    print(result)


class Networkerror(Exception):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print(e.args)
