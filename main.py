from telegram.ext import Application, MessageHandler, CommandHandler, filters
from random import randint

from assets.config import API
from utils import find_match, count_files_in_folder
from assets.text_scheme import scheme

# количество фоток кошек
COUNT_OF_CATS = count_files_in_folder('assets/cats')


# обработчик текста
async def get_answer(update, context):
    text = update.message.text
    for ITEM in scheme.keys():
        if find_match(text, scheme[ITEM]['list']):
            await update.message.reply_text(scheme[ITEM]['response'])
            return

    await update.message.reply_text(scheme['DEFAULT']['response'])


# обработчик отправки кошки
async def cat_command(update, context):
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(f'assets/cats/cat{randint(0, COUNT_OF_CATS - 1)}.png', 'rb'))


# обработчик /help
async def help_command(update, context):
    await update.message.reply_text(
        'Я понимаю команды <a>/help</a> и <a>/cat</a>, могу оценить фотокарточку,'
        ' а также очень доброжелательный!', parse_mode='HTML')


# обработчик получения фотографии
async def image_taking(update, context):
    await update.message.reply_text('Отличная фотокарточка!')


def main():
    application = Application.builder().token(API).build()

    text_handler = MessageHandler(filters.TEXT, get_answer)
    image_handler = MessageHandler(filters.PHOTO, image_taking)
    help_handler_command = CommandHandler("help", help_command)
    cat_handler_command = CommandHandler("cat", cat_command)

    application.add_handler(help_handler_command)
    application.add_handler(cat_handler_command)
    application.add_handler(text_handler)
    application.add_handler(image_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
