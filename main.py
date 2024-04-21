import telebot
token = '6556863084:AAEmML03j4T2VDIZN8c0b2czKkP14XWcsyE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Войдите /login")
@bot.message_handler(commands=["login"])
def send_welcome(message):
    print(message.from_user.id)
    bot.reply_to(message, "Ведите пороль")
    @bot.message_handler(content_types=['text'])
    def reverse_text(message):
        message

bot.polling()