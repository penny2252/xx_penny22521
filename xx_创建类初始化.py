class Cat():
    def __init__(self):
        print('这是一个初始化方法')
        # self.属性名=属性的初始值
        self.name = 'tom'


# 使用类名（）创建对象，会自动执行初始化方法__init__
tom = Cat()
print(tom.name)

