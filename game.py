import random
from typing import Tuple


MAX_TRIES_COUNT = 7
INTRO = f'''Добро пожаловать в игру угадай число, у вас ограниченное кол-во попыток({MAX_TRIES_COUNT}).
У вас так же есть возможность вызова подсказки, которая появится при вводе отправке 0 и затратит 1 попытку.'''


class Game:
    def __init__(self, max_tries=MAX_TRIES_COUNT):
        self._number_to_guess = None
        self._max_tries = max_tries
        self._tries = 0
        self.is_started = False

    def new_game(self) -> str:
        self._number_to_guess = random.randint(1, 100)
        self._tries = 0
        self.is_started = True
        return INTRO

    def try_guess(self, guess: str) -> Tuple[int, str]:
        if not self.is_started:
            return 0, 'Игра ещё не началась'

        try:
            guess = int(guess)
        except ValueError:
            return 0, 'Ошибка. Нужно ввести число'

        if self._tries >= self._max_tries:
            self.is_started = False
            return -1, 'Вы истратили все попытки, начните игру сначала!'

        self._tries += 1

        if guess == self._number_to_guess:
            self.is_started = False
            return 1, f'Поздравляю! Вы угадали число {self._number_to_guess} за {self._tries} попыток.'

        if guess == 0:
            clue = self._number_to_guess + random.randint(-10, 10)
            return 0, f'Загаданное число находится в диапазоне +-10 от {clue}'
        if guess < self._number_to_guess:
            return 0, 'Слишком мало! Попробуйте снова.'
        if guess > self._number_to_guess:
            return 0, 'Слишком много! Попробуйте снова.'
        if self._tries == self._max_tries:
            self.is_started = False
            return -1, 'Вы истратили все попытки, попробуйте снова!'



if __name__ == '__main__':

    test_game = Game()

    while True:
        if not test_game.is_started:
            print(test_game.new_game())
            continue

        try:
            guess = int(input('Введите число: '))
        except ValueError:
            print('Ошибка. Нужно ввести число')
            continue

        print(test_game.try_guess(guess))
        print()
