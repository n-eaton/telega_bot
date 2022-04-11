import constants as keys
from telegram.ext import *
import responses as res

print("Bot started...")


def start_command(update):
    update.message.reply_text('Type something random')


def help_command(update):
    update.message.reply_text('If you need help, please Google the question')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = res.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update{update} cased error{context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("start", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    dispatcher.add_error_handler(error)

    updater.start_polling(0)
    updater.idle()


main()
