class Cat:
    def eat(self):
        print('%s爱吃鱼' % self.name)

    def drick(self):
        print('%s爱喝水' % self.name)


tom = Cat()
tom.name = 'tom'
tom.drick()
tom.eat()
# print(tom)


lazy_cat = Cat()
lazy_cat.name = 'lazy_cat'
lazy_cat.eat()
lazy_cat.drick()
# print(lazy_cat)
