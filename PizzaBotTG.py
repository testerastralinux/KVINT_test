from PizzaBotAbstract import PizzaBotAbstract
from telegram import Update
from telegram.ext import Updater, CallbackContext, Filters
from telegram.ext import CommandHandler, MessageHandler


class PizzaBotTG(PizzaBotAbstract):
    def __init__(self, token):
        super().__init__()
        self.token = token

        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        self.dispatcher.add_handler(CommandHandler('start', self.__start_handler))
        self.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=self._get_message))

    def __start_handler(self, update: Update, context: CallbackContext):
        self._send_message(update, context)

    def _send_message(self, update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.messages[self.state])

    def _get_message(self, update: Update, context: CallbackContext):
        text = update.message.text
        update.message.reply_text(text)

    def run(self):
        self.updater.start_polling()
