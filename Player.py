from random import choice

class Player:

    MOVES=('rock','paper','scrissors')

    def __init__(self,is_computer=False):
        self.is_computer=is_computer


    def your_move(self):
        move=input('Enter your move: ')
        if move.lower() in Player.MOVES:
            return move
        else:
            print('please enter a valid move')
            self.your_move()

    def comp_move(self):
        if self.is_computer==True:
            cpu_chose=choice(Player.MOVES)
            print(f'computer choosed {cpu_chose}..')
            return cpu_chose
        else:
            return None






