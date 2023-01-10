import telebot
import random

bot = telebot.TeleBot('YOUR_TOKEN')

candys = 117
move = 'User'

def user_move(message):
    global candys
    global move
    if int(message.text) > 0 and int(message.text) < 29 and int(message.text) <= candys:
        candys -= int(message.text)
        move = 'Bot'
    else:
        bot.send_message(message.chat.id, 'Столько взять нельзя')


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Введите число не больше 28')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global candys
    global move
    user_move(message)
    bot.send_message(message.chat.id, f'На столе {str(candys)} конфет')
    move_candy = random.randint(1, 28)
    candys -= move_candy
    bot.send_message(message.chat.id, f'Bot взял {move_candy} конфет. Осталось {str(candys)} конфет')
    bot.send_message(message.chat.id, 'Введите число не больше 28')
    

bot.infinity_polling()
