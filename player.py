
from game import Game


class Player:
    def __init__(self, tg_id):
        self.tg_id = tg_id
        self.game = Game()

    def restart_game(self) -> str:
        return self.game.new_game()

    def try_guess(self, number):
        return self.game.try_guess(number)


if __name__ == '__main__':
    player = Player(0)

    print('Для начала новой игры введите "new_game"\n')
    while True:
        input_string = input()

        if input_string == 'new_game':
            print(player.restart_game())
        else:
            print(player.try_guess(input_string))
        print()
