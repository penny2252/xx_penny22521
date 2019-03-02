class Gun:
    def __init__(self, model, full_count):
        self.model = model
        self.full_count = full_count
        self.bullet_count = 0

    def reload(self):
        if self.bullet_count  > self.full_count:
            print('只能再装%d个子弹' % (self.full_count - self.bullet_count))
        print('装了%d个子弹'%(self.full_count - self.bullet_count))
        self.bullet_count += self.full_count - self.bullet_count

    def shoot(self):
        self.bullet_count -= 1
        print('ttt')


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def __str__(self):
        return ('%s的%s还有%d发子弹' % (self.name, self.gun.model, self.gun.bullet_count))

    def fire(self):
        if self.gun is None:
            print('还没有枪')
        elif self.gun.bullet_count<=0:
            print('没子弹了')
            return
        print('冲')
        self.gun.shoot()
        print ('%s的%s还有%d发子弹' % (self.name, self.gun.model, self.gun.bullet_count))


ak47 = Gun('AK47', 5)

xusanduo = Soldier('许三多')
xusanduo.gun = ak47
xusanduo.fire()
xusanduo.fire()
xusanduo.gun.reload()
xusanduo.fire()
xusanduo.fire()
xusanduo.fire()
xusanduo.fire()
xusanduo.fire()
xusanduo.fire()
print(xusanduo)