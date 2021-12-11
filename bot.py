from telegram.ext import Updater, CommandHandler
from request import request, session
import json

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')
    
def main(request=None):
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater("2135467205:AAHiY3EFCfUC5n6iZKBjIVHK3-ZCKAc7rSI", use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()



    url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parametors = {

        'slug':'bitcoin',
        convert

    }
   session = session

   