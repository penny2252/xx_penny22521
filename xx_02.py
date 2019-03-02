class Cat:
    def eat(self):
        print('%s爱吃鱼' % self.name)

    def drick(self):
        print('%s爱喝水' % self.name)


tom = Cat()
# tom.name = 'tom'
tom.drick()
tom.eat()
# print(tom)
# 在类外部添加属性的位置变化导致调用出错，不建议在类外部添加对象属性
tom.name = 'tom'

lazy_cat = Cat()
lazy_cat.name = 'lazy_cat'
lazy_cat.eat()
lazy_cat.drick()
# print(lazy_cat)
