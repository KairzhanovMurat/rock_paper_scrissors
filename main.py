from Player import Player
class Game:
    plr_wins = 0
    comp_wins = 0
    lim=0
    @classmethod
    def start_game(cls,player_one=True,player_two=False):
        plr_one=Player(player_one)
        plr_two=Player(player_two)
        print('Welcome to the rock paper scrissors game!')
        limit=int(input('Please enter the limit of the game: '))
        limit=Game.lim



        while True:
            answer=int(input('Would you like to play again?\n'
                         'press 1 if yes and 0 if no: '))
            if not answer:
                print('OK, good bye ))')
                break
            else:
                print('ok, lets go bruh')
            while True:
                ur_move=plr_two.your_move()
                cpu_move=plr_one.comp_move()
                if ur_move == 'rock':
                    if cpu_move=='paper':
                        Game.plr_wins+=1
                        print(f'You won {Game.plr_wins} : {Game.comp_wins}')
                        if cls._game_over():
                            break


                    elif cpu_move=='rock':
                        print('its a draw')
                    else:
                        Game.comp_wins+=1
                        print(f'You lost {Game.plr_wins} : {Game.comp_wins}')
                        if cls._game_over():
                            break
                        
                elif ur_move=='paper':
                    if cpu_move=='paper':
                        print('its a draw')
                    elif cpu_move=='scrissors':
                        Game.comp_wins+=1
                        print(f'You lost {Game.plr_wins} : {Game.comp_wins}')
                        if cls._game_over():
                            break
                    else:
                        Game.plr_wins+=1
                        print(f'You won {Game.plr_wins} : {Game.comp_wins}')
                        if cls._game_over():
                            break


                elif ur_move=='scrissors':
                    if cpu_move=='scrissors':
                        print('its a draw')
                    elif cpu_move=='rock':
                        Game.comp_wins+=1
                        print(f'You lost {Game.plr_wins} : {Game.comp_wins}')
                        if cls._game_over():
                            break
                    else:
                        Game.plr_wins+=1
                        print(f'You won {Game.plr_wins} : {Game.comp_wins}')
                        if cls._game_over():
                            break



    @classmethod
    def _game_over(cls):
        if Game.plr_wins>=Game.lim:
            print('Game over. You win!')
            return True
        elif Game.comp_wins>=Game.lim:
            print('You lost. Game over..')
            return True
        else:
            return False








Game.start_game()





