````pyton
from telegram.ext import Updater, CommandHandler
def start(update, context):
context.bot.send_message(chat_id=update.effective_chat.id, text="Assalomu alaykum! Botga xush kelibsiz!")
def main():
updater = Updater(token='6694456419:AAEInKwiPAYl9TolP6LRFHg5E5QABEr0Yv8') # TOKEN o'rniga o'zingizning botningizning API tokenini qo'ying
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
if __name__ == '__main__':
main()
````
