class Cat():

    # 可以增加多个属性名
    def __init__(self,new_name):
        # 自动执行
        print('这是一个初始化方法')
        # self.属性名=属性的初始值,
        #self.name = 'tom'
        self.name=new_name
    def eat(self):
        print('%s 爱吃鱼'%self.name)

# 使用类名（）创建对象，会自动执行初始化方法__init__
tom = Cat('tom')
print(tom.name)
tom.eat()
layz_cat=Cat('大毛')

layz_cat.eat()