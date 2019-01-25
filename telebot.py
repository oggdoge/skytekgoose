import telebot
import math 

token = '578244051:AAFmsZ1tgJF-5UeyEbEijAa-5soAxpf15-A'
bot = telebot.TeleBot(token)

key = telebot.types.InlineKeyboardMarkup()
basket = telebot.types.InlineKeyboardButton(text='Корзина', callback_data='basket')
items=telebot.types.InlineKeyboardButton(text='Ассортимент',callback_data='items')
support=telebot.types.InlineKeyboardButton(text='Поддержка',callback_data='support')
key.row(items,basket)
key.row(support)

@bot.message_handler(commands=['start'])
def handle_start(message):
  
  bot.send_message(message.chat.id, 'Так это и будет выглядеть',reply_markup=key)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  if call.data=='basket':
    #bot.send_message(message.chat.id, 'Тут должна быть корзина. Пока нет.',reply_markup=key)
    bot.answer_callback_query(callback_query_id=call.id,show_alert=False,text='Вы выбрали корзину')

