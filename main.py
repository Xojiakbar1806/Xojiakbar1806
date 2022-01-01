import telebot
from pytube import YouTube
import glob
import requests
import os
token = '5011490665:AAGC8IlabdbOupf_0NTG6mWySiQoN5PHGCo'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Salom! YouTube link yuborishingiz mumkin.')

@bot.message_handler(func=lambda message: True)
def start_message(message):
    if 'youtu' in message.text:
      global link
      link = message.text
      yt = YouTube(link).streams
      ls=[]
      for i in range(len(yt)):
        sstr=str(yt[i])
        try:
          nextt=sstr[sstr.index('res="')+5:]
          if (nextt[:4] not in ls) and str(nextt[:4])[-1]=='p':
            ls.append(nextt[:4])
        except:
          pass
      markup = telebot.types.InlineKeyboardMarkup()
      for i in range(len(ls)):
        markup.add(telebot.types.InlineKeyboardButton(text=ls[i], callback_data=ls[i]))

      if yt.filter(type='audio'):
          markup.add(telebot.types.InlineKeyboardButton(text='Audio', callback_data='audio'))
      bot.send_message(message.chat.id, text=YouTube(link).title+':', reply_markup=markup)
    else:
      bot.send_message(message.chat.id, text="Iltimos YouTube link yuboring.")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Tasdiqlandi!')
    bot.send_message(call.message.chat.id, 'Kuting...')
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    bot.delete_message(call.message.chat.id,call.message.message_id)
    if call.data == 'audio':
        YouTube(link).streams.filter(type='audio').first().download('videoo')
        list_of_files = glob.glob('videoo//*')
        mp3 = open(max(list_of_files, key=os.path.getctime), "rb")
        try:
            bot.send_audio(call.message.chat.id, mp3)
        except:
            bot.send_message(call.message.chat.id, 'Boshqa urinib ko`ring ')
    else:
        YouTube(link).streams.filter(res=call.data).first().download('videoo')
        list_of_files = glob.glob('videoo//*')
        video = open(max(list_of_files, key=os.path.getctime), "rb")
        try:
            bot.send_video(call.message.chat.id, video)
        except:          
            bot.send_message(call.message.chat.id, 'Boshqa urinib ko`ring ')
    os.remove(min(glob.glob('videoo//*'), key=os.path.getctime))
bot.infinity_polling()
