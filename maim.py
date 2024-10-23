#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import random
import os


API_TOKEN = '7876846172:AAGNehL8YkrvbZJrMg9ykt2n3hQrcKXguPw'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет я чатер бот")
    



@bot.message_handler(commands=['gif'])
def send_welcome(message):
    bot.reply_to(message, 'GIF')
    bot.send_animation(message.chat.id, "https://www.gifcen.com/wp-content/uploads/2023/04/sigma-gif-9.gif")




@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,"Мои команды на данный момент start и gif" )


@bot.message_handler(commands=["mem","meme"])
def send_meme(message):
    image = random.choice(os.listdir("images"))
    with open("images/" + image, "rb") as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=["animal","animals"])
def send_animal(message):
    image = random.choice(os.listdir("animals"))
    with open("animals/" + image, "rb") as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=["trash"])
def send_welcome(message):
    trash = [
    "ежегодно человек выбрасывает около 2 тоннн.",
    "мусор вызывает существенные изменения климата и постоянно загрязняет окружающую среду.",
    "Пластиковые отходы могут разлагаться до 1 тыс. лет."
    ]
    fact = random.choice(trash)
    bot.reply_to(message,fact)

@bot.message_handler(commands=["trash_meme"])
def send_trash(message):
    image = random.choice(os.listdir("tras"))
    with open("tras/" + image, "rb") as f:
        bot.send_photo(message.chat.id, f)



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
