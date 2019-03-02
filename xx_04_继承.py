class Animal:
    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')


# 继承在子类的名称后加上父类名称

class Dog(Animal):
    def bark(self):
        print('叫')
class Cat(Animal):
    def catch(self):
        print('抓')
#可以多继承
class TianDog(Dog,Cat):

    def fly(self):
        print('飞')

    def bark(self):
        print('天狗叫')

    def eat(self):
        print('大吃')
        #利用super（）调用父类中的方法
        super().eat()
        print('*'*10)
        #利用父类.方法（self）同样可以调用父类方法(2.0中的方法)
        Animal.eat(self)

        print('*' * 10)




xiaotian = TianDog()
xiaotian.run()
xiaotian.eat()
xiaotian.drink()
xiaotian.fly()
xiaotian.bark()
xiaotian.catch()
kitty=Cat()
kitty.eat()

