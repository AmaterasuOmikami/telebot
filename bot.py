
import telebot
from player import Player


TOKEN = "6508897025:AAEasPzTvF7s1ss5Dde_uqWT6RYaU1O6lCc"
memory: dict[int, Player] = {}
bot = telebot.TeleBot(TOKEN)


def get_player(tg_id) -> Player:
    if tg_id not in memory:
        memory[tg_id] = Player(tg_id)

    return memory[tg_id]
    

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет\nДля начала новой игры используй команду /new_game")
    memory[message.chat.id] = Player(message.chat.id)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Для начала новой игры используй команду /new_game")


@bot.message_handler(commands=['new_game'])
def new_game_command(message):
    player = get_player(message.chat.id)
    bot.send_message(message.chat.id, player.restart_game())


@bot.message_handler()
def text_message(message):
    player = get_player(message.chat.id)
    bot.send_message(message.chat.id, player.try_guess(message.text))
