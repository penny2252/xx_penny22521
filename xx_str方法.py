# str显示对象自定义信息,这个方法必须返回字符串
class Cat():
    def __init__(self, new_name):
        self.name = new_name
        print('%s来了' % self.name)

    def __str__(self):
        return '我是小猫[%s]' % self.name


tom = Cat('tom')
print(tom)
