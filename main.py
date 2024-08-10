import random


number_to_guess = random.randint(1, 100)
guess = 10
tries = 0
MAX_TRIES_COUNT = 15
info = f'''Добро пожаловать в игру угадай число, у вас ограниченное кол-во попыток({MAX_TRIES_COUNT}).
У вас так же есть возможность вызова подсказки, котороя появится при вводе отправке 0 
и затратит 1 попытку.'''

print(info)
print("Угадай число от 1 до 100")
while guess != number_to_guess:
    try:
        guess = int(input("Введите число: "))
    except ValueError:
        print("Ошибка. Нужно ввести число")
        continue

    tries += 1
    if guess == 0:
        clue = number_to_guess + random.randint(-10, 10)
        print(f"Загаданное число находится в диапазоне +-10 от {clue}")
    elif guess < number_to_guess:
        print("Слишком мало! Попробуй снова.")
    elif guess > number_to_guess:
        print("Слишком много! Попробуй снова.")
    elif tries == MAX_TRIES_COUNT:
        print('Вы истратили все попытки, попробуйте снова!')
        break
    print(f'Использовано {tries} попыток.')
else:
    print(f"Поздравляю! Вы угадали число {number_to_guess} за {tries} попыток.")
