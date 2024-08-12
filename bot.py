
import telebot
from typing import Dict
from player import Player
from config import TOKEN, TG_ADMINS


HELP = 'Для начала новой игры используй команду /new_game\nДля вывода статистики /statistic'

memory: Dict[int, Player] = {}
bot = telebot.TeleBot(TOKEN)


def get_player(tg_id) -> Player:
    return memory[tg_id]


def add_player(tg_id, first_name, last_name, username):
    memory[message.chat.id] = Player(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Привет\n' + HELP)
    add_player(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['new_game'])
def new_game_command(message):
    player = get_player(message.chat.id)
    bot.send_message(message.chat.id, player.start_new_game())


@bot.message_handler(commands=['statistic'])
def statistic_command(message):
    player = get_player(message.chat.id)
    bot.send_message(message.chat.id, player.get_statistic())


@bot.message_handler(commands=['about_all'])
def about_all_command(message):
    if message.chat.id not in TG_ADMINS:
        bot.send_message(message.chat.id, 'У вас недостаточно прав')
        return

    response = []
    for tg_id, player in memory.items():
        response.append(f'{tg_id};\n{player.get_statistic()};\n{player.get_about()}')
    bot.send_message(message.chat.id, '\n----\n'.join(response))


@bot.message_handler()
def text_message(message):
    player = get_player(message.chat.id)
    bot.send_message(message.chat.id, player.try_guess(message.text))
