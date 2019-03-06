class Game(object):


    top_score= 100

    def __init__(self, name):
        self.name = name
    #静态方法
    @staticmethod
    def show_help():
        print('***')
    #类方法
    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    def start_game(self):
        Game.show_help()
        Game.show_top_score()
        print('开始%s的游戏' % self.name)

xx = Game('XX')

xx.start_game()
