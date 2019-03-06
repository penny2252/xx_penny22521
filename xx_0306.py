class Abc(object):
    isinstance=None
    def __new__(cls, *args, **kwargs):
        cls.isinstance=super().__new__(cls)
        return cls.isinstance
    # def __init__(self):
    #     print('a')


a = Abc()
print(a)
b = Abc()
print(b)
