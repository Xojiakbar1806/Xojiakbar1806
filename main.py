from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext.updater import Updater
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from translate import Translator
token="5012516652:AAFrWxVocdjGRsLAI61Mpz1DeTl5Wf6rmJQ"
def sellect_lang(update: Update, context: CallbackContext) -> None:
	keyboard = [
		[
			InlineKeyboardButton("🇺🇿 O'zbek tili ➡️ 🇬🇧 Ingliz tili", callback_data="EN")
		],
		[
			InlineKeyboardButton("🇺🇿 O'zbek tili ➡️ 🇷🇺 Rus tili", callback_data="RU"),
		],
		[
			InlineKeyboardButton("🇬🇧 Ingliz tili ➡️ 🇺🇿 O'zbek tili", callback_data="en-uz")
		],
		[
			InlineKeyboardButton("🇷🇺 Rus tili ➡️ 🇺🇿 O'zbek tili", callback_data="ru-uz")
		],
	]
	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text('Qaysi tildan qaysi tilga tarjima qilmoqchisiz?', reply_markup=reply_markup)
lang = ""
def button(update: Update, context:CallbackContext) -> None:
	global lang
	lang = update.callback_query.data.lower()
	query = update.callback_query
	query.answer()
	if query.data == "ru-uz":
		query.edit_message_text(text="🇷🇺 Rus tili ➡️ 🇺🇿 O'zbek tilini tanladingiz, har bir yuborgan so'zingizni Rus tilidan O'zbek tiligaga tarjima qilib beraman. So'z yuborishingiz mumkin.\nTilni o'zgartirish uchun '/sellect_lang' ni yuboring")
	elif query.data == "en-uz":
		query.edit_message_text(text="🇬🇧 Ingliz tili ➡️ 🇺🇿 O'zbek tilini tanladingiz, har bir yuborgan so'zingizni Ingliz tilidan O'zbek tiligaga tarjima qilib beraman. So'z yuborishingiz mumkin.\nTilni o'zgartirish uchun '/sellect_lang' ni yuboring")
	elif query.data == "RU":	
		query.edit_message_text(text="🇺🇿 O'zbek tili ➡️ 🇷🇺 Rus tilini tanladingiz, har bir yuborgan so'zingizni O'zbek tilidan Rus tiligaga tarjima qilib beraman. So'z yuborishingiz mumkin.\nTilni o'zgartirish uchun '/sellect_lang' ni yuboring")
	elif query.data == "EN":	
		query.edit_message_text(text="🇺🇿 O'zbek tili ➡️ 🇬🇧 Ingliz tilini tanladingiz, har bir yuborgan so'zingizni O'zbek tilidan Ingliz tiligaga tarjima qilib beraman. So'z yuborishingiz mumkin.\nTilni o'zgartirish uchun '/sellect_lang' ni yuboring")		
def lang_translator(user_input):
	if lang == "ru-uz":
		translator = Translator(from_lang = "RU", to_lang = "UZ")
	elif lang == "en-uz":
		translator = Translator(from_lang = "EN", to_lang = "UZ")
	else:
		translator = Translator(from_lang = "UZ", to_lang = lang)
	translation = translator.translate(user_input)
	return translation
def reply(update ,context):
	user_input = update.message.text
	update.message.reply_text(lang_translator(user_input) + "\n\n @Tarjimon_en_ru_bot")
def main():
	updater = Updater(token, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', sellect_lang))
	dp.add_handler(CommandHandler('sellect_lang',sellect_lang))
	dp.add_handler(CallbackQueryHandler(button))
	dp.add_handler(MessageHandler(Filters.text, reply))
	updater.start_polling()
	updater.idle()
main()