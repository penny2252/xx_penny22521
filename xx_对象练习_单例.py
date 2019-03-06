class MusicPlayer(object):
    isinstance=None
    init_flag=False
    def __new__(cls, *args, **kwargs):
        if  cls.isinstance is None:
            cls.isinstance=super().__new__(cls)
        return cls.isinstance
    def __init__(self):
        if self.init_flag ==False:
            print('a')
            self.init_flag=True


player1=MusicPlayer()
print(player1)
player2=MusicPlayer()
print(player2)