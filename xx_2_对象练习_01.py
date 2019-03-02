class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        # print('%s体重%d' % (self.name, self.weight))

    def __str__(self):
        return '我的名字是%s,体重是%.2f公斤'%(self.name,self.weight)

    def run(self, time_run):
        self.run_times= time_run
        self.weight -= time_run * 0.5
        print('%s跑步%d次减重%.2f公斤，现在重%.02f公斤' % (self.name, self.run_times, self.run_times * 0.5, self.weight))

    def eat(self, time_eat):
        self.eat_times = time_eat
        self.weight += time_eat * 1
        print('%s吃饭%d次增重%.2f公斤，现在重%.2f公斤' % (self.name, self.eat_times, self.eat_times* 1, self.weight))


xiaoming=Person('小明', 75)
xiaoming.run(5)
xiaoming.eat(5)
print(xiaoming)
xiaomei=Person('小美',45)
xiaomei.run(4)
xiaomei.eat(4)
print(xiaomei)
