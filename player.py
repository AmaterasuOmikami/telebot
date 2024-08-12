
from game import Game


class Player:
    def __init__(self, tg_id, first_name, last_name, username):
        self.tg_id = tg_id
        self.game = Game()
        self.wins = 0
        self.loses = 0
        self.games = 0
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def start_new_game(self) -> str:
        if self.game.is_started:
            self.loses += 1

        self.games += 1
        return self.game.new_game()

    def try_guess(self, number):
        status, response = self.game.try_guess(number)
        if status > 0:
            self.wins += 1
        elif status < 0:
            self.loses += 1

        return response

    def get_statistic(self) -> str:
        return f'Игр: {self.games}; Побед: {self.wins}; Поражений: {self.loses};'

    def get_about(self) -> str:
        return f'Имя: {self.first_name}; Фамилия: {self.last_name}; Username: {self.username};'


if __name__ == '__main__':
    player = Player(0, 'a', 'b', 'c')

    print('Для начала новой игры введите "new_game"\n')
    while True:
        input_string = input()

        if input_string == 'new_game':
            print(player.start_new_game())
        elif input_string == 'statistic':
            print(player.get_statistic())
        else:
            print(player.try_guess(input_string))
        print()
