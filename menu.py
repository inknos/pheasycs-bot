from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_menu():
    keyboard = [[InlineKeyboardButton("Create Event", callback_data="create_event"),
                 InlineKeyboardButton("Ask Calendar", callback_data="ask_calendar")],

                [InlineKeyboardButton("Info", callback_data="info")]]

    return (InlineKeyboardMarkup(keyboard), "Main Menu")

def set_priority_menu():
    keyboard = [[InlineKeyboardButton("Low Priority", callback_data="low_priority")],
                [InlineKeyboardButton("Normal", callback_data="normal_priority")],
                [InlineKeyboardButton("High Priority", callback_data="high_priority")]]

    return (InlineKeyboardMarkup(keyboard), "Select Event Priority")
