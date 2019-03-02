class XiaoXiao:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print('%s的年龄是%d' % (self.name, self.__age))


xiaoxiao = XiaoXiao('晓晓')
# 程序外部不可以访问私有属性
# print(xiaoxiao._age)
# 所谓私有是伪私有，可以通过在私有属性前加(_类名)从外部访问私有属性
print(xiaoxiao._XiaoXiao__age)
# 程序外部不可以访问私有方法
# xiaoxiao.__secret()
# 所谓私有是伪私有，可以通过在私有方法前加(_类名)从外部访问私有方法
xiaoxiao._XiaoXiao__secret()
