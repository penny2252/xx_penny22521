class Abc(object):
    isinstance=None
    def __new__(cls, *args, **kwargs):
        if cls.isinstance==None:
            cls.isinstance=super().__new__(cls)

        return cls.isinstance
    # def __init__(self):
    #     print('a')


a = Abc()
b = Abc()
print(a)

print(b)
