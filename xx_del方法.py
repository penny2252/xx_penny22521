class Cat():
    def __init__(self,new_name):
        self.name=new_name
        print('%s 来了'%self.name)
    def __del__(self):
        print('%s 去了'%self.name)
tom=Cat('tom')
print(tom.name)
# del 把tom当做对象删除
del tom
#如果不执行del tom 在执行下面print命令后没有可以执行的命令，tom也会自动删除，并显示‘走了’
print('-'*50)