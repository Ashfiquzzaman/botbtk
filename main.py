import telebot
import time

TOKEN="1692681867:AAGqsrY3KNomUKzhp3bFBtXW3h6a7L5X1bQ"
bot=telebot.Telebot(TOKEN)

@bot.message_handler(commands=["start"])

def start(message):
print(message.text)


@bot.message_handler(commands=["hello",["hi"])

def hello(message):
bot.send_message(messege.chat.id, "Hello world")

while True:
try:
bot.polling()
except:
time.sleep(5)
