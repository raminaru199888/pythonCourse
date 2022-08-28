from telegram import InlineKeyboardButton, Update, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram.ext.updater import Updater
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from translate import Translator


def language_selection(update: Update, context: CallbackContext) -> None:
    keypad = [
        [
            InlineKeyboardButton('Ukrainian', callback_data="Ukrainian"),
            InlineKeyboardButton('English', callback_data="English"),
            InlineKeyboardButton('German', callback_data="German"),
            InlineKeyboardButton('Chinese', callback_data="Chinese")
        ]
    ]
    response_markup = InlineKeyboardMarkup(keypad)
    update.message.reply_text('Привет! Выберите язык для перевода. Родной язык: русский!', reply_markup=response_markup)
translation_into = ''

def button_functionality(update: Update, context: CallbackContext) -> None:
    global translation_into
    translation_into = update.callback_query.data.lower()
    request = update.callback_query
    request.answer()
    request.edit_message_text(text=f'{request.data} язык выбран. Введите свой текст!')

def language_translator(user_input):
    translator = Translator(from_lang='russian', to_lang=translation_into)
    translation = translator.translate(user_input)
    return translation

def response_for_user(update, context):
    user_input = update.message.text
    update.message.reply_text(language_translator(user_input))
    # if user_input == "ТЕКСТ": # обработать ошибку при некорректном вводе
    #     update.message.reply_text(f'Привет! Я бот-переводчик...')
    # else:
    #     update.message.reply_text('Я вас не понял!')

def main_menu():
    updater = Updater('5483954774:AAGfqgJSTuMrTyjeIBdxC1VSrRTCd0dpzmI', use_context=True)
    menu = updater.dispatcher
    menu.add_handler(CommandHandler('start', language_selection))
    menu.add_handler(CommandHandler('select_lang', language_selection))
    menu.add_handler(CallbackQueryHandler(button_functionality))
    menu.add_handler(MessageHandler(Filters.text, response_for_user))
    updater.start_polling()
    updater.idle()
main_menu()
