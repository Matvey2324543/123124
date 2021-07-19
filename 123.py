import telebot, time
# from telebot import types
import wikipedia
import sqlite3 

wikipedia.set_lang("ru")

bot = telebot.TeleBot('1889452037:AAGKDQqaaytFIqIyZ-unqr8wyJE9wyIhot4')

print('Start')


@bot.message_handler(commands=['wikipedia'])
def send_start_message(message):
    bot.send_message(message.chat.id, 'Привет, это википедия, пиши любое слово и я найду его определение. ')


@bot.message_handler(content_types=['text'])
def HELP(message):
    message_text = message.text.lower()
    if message_text == 'привет' or message_text == 'ку':
        bot.send_message(message.chat.id, 'Привет')
    else:
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        check = cursor.execute(f'SELECT * from people where id = "{message.from_user.id}"').fetchall()
        if len(check) == 0:
            cursor.execute(f'insert into people values ("{message.from_user.id}", "{message.from_user.first_name}", 1)')
        else:
            cursor.execute(f'UPDATE people SET number_of_requests = number_of_requests + 1 where id = "{message.from_user.id}"')
        connect.commit()
        bot.send_message (message.chat.id,wikipedia.summary(message_text, sentences=5))
    print(message.chat.id)
    print(message.from_user.id)
    print(message.message_id)
    # bot.edit_message_text(chat_id=message.chat.id, text = ':cold_face:', message_id = 141)
    # bot.delete_message(chat_id = message.chat.id, message_id = message.message_id+1)
    # bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
    # print(message)

    # print(message.text)






while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(1)









