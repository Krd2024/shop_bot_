import sqlite3
import telebot
from telebot import types
from wrapper_bot import TelegramBotWrapper
from utils import category
from decouple import config

TOKEN = config("TOKEN", cast=str, default="пусто")

bot = TelegramBotWrapper(TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    print("Start message")
    uid = message.chat.id
    category(uid)
