# Conversational Games Bot for Telegram.
# Last updated 13-01-2021

## Imports.
# Telegram (API Wrapper)
from telegram import ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, InlineQueryHandler, CallbackContext, CallbackQueryHandler
from telegram.utils.helpers import escape_markdown

# HTTP Requests & Parsing
import requests
import html
import json

# Randomization
from random import choice

## Constants
# Load the config.json into a 'CONFIG' variable.
with open('config.json') as f:
	CONFIG = json.load(f)

# The inline keyboard markup for the two buttons (Red and Blue).
# Used in: Would You Rather, Will You Press The Button, and This Or That.
RED_BLUE_KEYBOARD = InlineKeyboardMarkup([[
	InlineKeyboardButton("🔴", callback_data = 'red'),
	InlineKeyboardButton("🔵", callback_data = 'blue')
]])

## Info.
print("=" * 25)
print("Conversational Games Bot")
print("=" * 25)
print("1.0.0 | Release | By Sendi", '\n')

## Functions.
def parse_list_file(file_path: str) -> list:
	"""Parse a text file into a list containing each line."""
	
	with open(file_path) as f:
		return [l.strip() for l in f.readlines() if l.strip()]

print("[Loading] Loading responses...")
# Open all the text files and load them into list variables in a dictionary.
database = {
	"truths": parse_list_file('data/truths.txt'),
	"dares": parse_list_file('data/dares.txt'),
}

## Setup.
print("[Set-Up] Setting up bot..")
updater = Updater(token = CONFIG['BOT_TOKEN'])
dispatcher = updater.dispatcher

## Commands.
def c_start(update: Update, ctx: CallbackContext) -> None:
	"""General info about the bot and command help."""
	
	text = (
		"Ini adalah bot TrutOrDare khusus untuk grup, kirim command di grup.",
	)
	ctx.bot.send_message(chat_id = update.effective_chat.id, text = '\n'.join(text))

def c_truth(update: Update, ctx: CallbackContext) -> None:
	"""Get a truth question."""
	
	response = f"*Truth:* {escape_markdown(choice(database['truths']), 2)}"
	ctx.bot.send_message(chat_id = update.effective_chat.id, text = response, parse_mode=ParseMode.MARKDOWN_V2)
        reply_to_message_id=message.message_id
    ) 

def c_dare(update: Update, ctx: CallbackContext) -> None:
	"""Get a dare."""
	
	response = f"*Dare:* {escape_markdown(choice(database['dares']), 2)}" 
	ctx.bot.send_message(chat_id = update.effective_chat.id, text = response, parse_mode=ParseMode.MARKDOWN_V2)
        reply_to_message_id=message.message_id
    ) 

def c_donasi(update: Update, ctx: CallbackContext) -> None:
	"""General info about the bot and command help."""
	
	text = (
		"Jika anda menyukai Bot ini dan ingin memberikan donasi serta dukungan agar Bot ini tetap aktif, Bisa melalui link dibawah ini :",
		"https://t.me/TeleDonateSen",
	)
	ctx.bot.send_message(chat_id = update.effective_chat.id, text = '\n'.join(text))
        reply_to_message_id=message.message_id
    ) 

def c_help(update: Update, ctx: CallbackContext) -> None:
	"""General info about the bot and command help."""
	
	text = (
		"✿Perintah Untuk Bot TrutOrDare✿\n",
		"/dare atau /d : Memberikan Tantangan",
		"/truth atau /t : Memberikan Pertanyaan",
		"/donasi : Memberikan Donasi Atau Dukungan",
		"/help : Bantuan\n",
		"✿Untuk Request TrutOrDare Bisa Klik Bot @RequestTrutDare_Bot",
	)
	ctx.bot.send_message(chat_id = update.effective_chat.id, text = '\n'.join(text))
        reply_to_message_id=message.message_id
    ) 

## Command Handler.
print("[Set-Up] Adding handlers..")
# -- Command Handler -- 
dispatcher.add_handler(CommandHandler(('start'), c_start))
dispatcher.add_handler(CommandHandler(('t', 'truth'), c_truth))
dispatcher.add_handler(CommandHandler(('d', 'dare'), c_dare))
dispatcher.add_handler(CommandHandler(('donasi'), c_donasi))
dispatcher.add_handler(CommandHandler(('help'), c_help))
# -- Callback Query Handler --

## Polling / Login.
updater.start_polling()
print("[Ready] Bot is ready. Started polling.")
