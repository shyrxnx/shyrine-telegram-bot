from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime


TOKEN: Final = '6895369183:AAF9mSB0QJYmWzInb82a1VXIdW6bmKJTqhs'
BOT_USERNAME: Final = '@shyrxnx_bot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello! I'm a Shyrine's Bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Honey, ask Shyrine for help!")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"This is a custom command. It literally doesn't do anything :D")


# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return "Hey! How's life for you?"

    if 'hi' in processed:
        return "Hey! How's life for you?"

    if 'good morning' in processed:
        return "Hey! How's life for you?"

    if 'good afternoon' in processed:
        return "Hey! How's life for you?"

    if 'good evening' in processed:
        return "Hey! How's life for you?"

    if 'good day' in processed:
        return "Hey! How's life for you?"

    if 'who' in processed:
        return "I am Shyrine Bot created by Shyrine Salvador!"

    if 'who are you' in processed:
        return "I am Shyrine Bot created by Shyrine Salvador!"

    if 'who are you?' in processed:
        return "I am Shyrine Bot created by Shyrine Salvador!"

    if 'what are you' in processed:
        return "I am Shyrine Bot created by Shyrine Salvador!"

    if 'what are you?' in processed:
        return "I am Shyrine Bot created by Shyrine Salvador!"

    if 'how are you' in processed:
        return "I am doing good! Thank you for asking."

    if 'time' in processed:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if 'time?' in processed:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if 'what is the time?' in processed:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if 'current time' in processed:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if 'current time?' in processed:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "Pardon, I don't quite understand you."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print("Polling....")
    app.run_polling(poll_interval=1)
