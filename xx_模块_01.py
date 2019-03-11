#1、一般情况下的使用方法
# import xx_模块_测试01
# import xx_模块_测试02
#
# xx_模块_测试01.mod1()
# xx_模块_测试02.mod2()
#
# dog=xx_模块_测试02.Dog()
# cat=xx_模块_测试01.Cat()
#
# print(dog)
# print(cat)


#2、可以对模块设置别名，别名应符合大驼峰方法
# import xx_模块_测试01 as TestModule1
# import xx_模块_测试02 as TestModule2
#
# TestModule1.mod1()
# TestModule2.mod2()
#
# dog=TestModule2.Dog()
# cat=TestModule1.Cat()
# print(dog)
# print(cat)


#3、只希望导入一部分函数，可以用from方法,调用函数时可以不需要模块名字直接调用函数
#如果导入的两个函数的名称一样，那么第一个导入的将被覆盖
# from xx_模块_测试01 import mod1
# from xx_模块_测试02 import mod2
#
# mod1()
# mod2()
#
# from xx_模块_测试01 import Cat as dog
# from xx_模块_测试02 import Dog as cat
# dog1=dog()
# cat1=cat()
# print(dog1)
# print(cat1)

#4导入模块中所有函数,但不建议使用
from xx_模块_测试02 import *
dog=Dog()
print(dog)