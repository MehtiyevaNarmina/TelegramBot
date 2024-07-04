import json
from typing import Final
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application
TOKEN: Final = '7453578231:AAGuAQIfsqdQxJhtn7QUFxQ9b61w6v8nE30'
BOT_USERNAME: Final = "@bun_sun_tulip_bot"

#Set commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!')
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('How can i help you?')
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Custom')
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

#Json file to dictionary
def definitions (json_file):
    with open('data.json') as f:
        data = json.load(f)
        return definitions

#get definitions of words from dictionary
def get_definitions(word,definitions):
    definition = {key.lower(): value for key,value in definitions.items()}
    return definition


#Response tob messages
def type_definitions():
    
    if __name__ == '__main__':
        print('Starting bot...')
        application =  Application.builder().token(TOKEN).build()

# Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("custom", custom_command))
    
    # Message handler for all text messages
    application.add_handler(MessageHandler(filters.TEXT, response))
  
    # Errors
    application.add_error_handler(error)
    # Polls 
    print('Polling...')
    application.run_polling(poll_interval=5)
