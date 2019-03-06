class MusicPlayer(object):
    def __new__(cls, *args,**kwargs):
        print('fenpeikongjian')
        instance=super().__new__(cls)
        return instance

    def __init__(self):
        print('bofangqi')

player=MusicPlayer()

print(player)
player2=MusicPlayer()
print(player2)