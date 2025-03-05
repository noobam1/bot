import telebot
from telebot import types

# Replace this with your bot's API token
TOKEN = '7607875303:AAFcPDtbxKbgWrv3NeqSN-wNKicyRd_tPUk'

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Create a function to send a custom keyboard
def create_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    id_button = types.KeyboardButton("🪪 ID")
    group_button = types.KeyboardButton("Group 🪪")
    markup.add(id_button, group_button)
    return markup

# Function to handle the "/start" command and show the keyboard
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome! Please choose an option:", reply_markup=create_keyboard())

# Function to handle when the user clicks the "🪪 ID" button
@bot.message_handler(func=lambda message: message.text == "🪪 ID")
def send_chat_id(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, f"Your chat ID is: {chat_id}")

# Function to handle when the user clicks the "Group 🪪" button
@bot.message_handler(func=lambda message: message.text == "Group 🪪")
def ask_for_group(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    group1_button = types.KeyboardButton("Group 1")
    group2_button = types.KeyboardButton("Group 2")
    group3_button = types.KeyboardButton("Group 3")
    back_button = types.KeyboardButton("Back")
    markup.add(group1_button, group2_button, group3_button, back_button)
    bot.send_message(message.chat.id, "Please choose a group:", reply_markup=markup)

# Function to handle group selection
@bot.message_handler(func=lambda message: message.text in ["Group 1", "Group 2", "Group 3"])
def handle_group_selection(message):
    bot.send_message(message.chat.id, f"You chose {message.text}. Here are the group details...")
    # You can add your specific group-related actions or details here

# Function to handle the "Back" button press
@bot.message_handler(func=lambda message: message.text == "Back")
def go_back(message):
    bot.send_message(message.chat.id, "Please choose an option:", reply_markup=create_keyboard())

# Start polling for new messages
bot.polling()