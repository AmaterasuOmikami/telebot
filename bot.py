
import telebot
from typing import Dict
from player import Player
from config import TOKEN


memory: Dict[int, Player] = {}
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
