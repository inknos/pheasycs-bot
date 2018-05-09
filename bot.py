#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import environ
root = environ.Path(__file__)
env = environ.Env(DEBUG=(bool, False),) # set default values and casting
environ.Env.read_env() # reading .env file

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("Create Event", callback_data='Create Event'),
                 InlineKeyboardButton("Ask Calendar", callback_data='Ask Calendar')],

                [InlineKeyboardButton("Nothing", callback_data='Nothing')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Main Menu', reply_markup=reply_markup)

def main_menu(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="{}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
    
def create_event_menu(bot, update):
    keyboard = [[InlineKeyboardButton("", callback_data='Create Event'),
                 InlineKeyboardButton("Ask Calendar", callback_data='Ask Calendar')],

                [InlineKeyboardButton("Nothing", callback_data='Nothing')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Create Event', reply_markup=reply_markup)


def show_calendar_menu(bot, update):
    keyboard = [[InlineKeyboardButton("Ask for available days", callback_data='Available Days'),
                 InlineKeyboardButton("Ask Info", callback_data='Info')],

                [InlineKeyboardButton("back", callback_data='back')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Show Calendar', reply_markup=reply_markup)

def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(env("TOKEN"))

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
