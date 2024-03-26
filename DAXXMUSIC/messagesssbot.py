from telegram.ext import Updater, MessageHandler, Filters
from telegram import ChatPermissions

# Replace 'YOUR_API_TOKEN' with your actual API token obtained from BotFather


def delete_message(update, context):
    """Delete message containing 'pagal' in usernames"""
    message = update.message
    if message and message.from_user and 'pagal' in message.from_user.username.lower():
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        # Restrict the user from sending messages for a while
        context.bot.restrict_chat_member(chat_id=message.chat_id, user_id=message.from_user.id, permissions=ChatPermissions())
        # Send warning message to the user
        context.bot.send_message(chat_id=message.chat_id, text=f"@{message.from_user.username} you have been warned, abusive language is not allowed.")




def delete_message(update, context):
    """Delete message containing 'pagal' in usernames"""
    message = update.message
    if message and message.from_user and 'pagal' in message.from_user.username.lower():
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        # Restrict the user from sending messages for a while
        context.bot.restrict_chat_member(chat_id=message.chat_id, user_id=message.from_user.id, permissions=ChatPermissions())
        # Send warning message to the user
        context.bot.send_message(chat_id=message.chat_id, text=f"@{message.from_user.username} you have been warned, abusive language is not allowed.")



def delete_message(update, context):
    """Delete message containing 'pagal' in usernames"""
    message = update.message
    if message and message.from_user and 'pagal' in message.from_user.username.lower():
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        # Restrict the user from sending messages for a while
        context.bot.restrict_chat_member(chat_id=message.chat_id, user_id=message.from_user.id, permissions=ChatPermissions())
        # Send warning message to the user
        context.bot.send_message(chat_id=message.chat_id, text=f"@{message.from_user.username} you have been warned, abusive language is not allowed.")



def delete_message(update, context):
    """Delete message containing 'pagal' in usernames"""
    message = update.message
    if message and message.from_user and 'pagal' in message.from_user.username.lower():
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        # Restrict the user from sending messages for a while
        context.bot.restrict_chat_member(chat_id=message.chat_id, user_id=message.from_user.id, permissions=ChatPermissions())
        # Send warning message to the user
        context.bot.send_message(chat_id=message.chat_id, text=f"@{message.from_user.username} you have been warned, abusive language is not allowed.")



def delete_message(update, context):
    """Delete message containing 'pagal' in usernames"""
    message = update.message
    if message and message.from_user and 'pagal' in message.from_user.username.lower():
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        # Restrict the user from sending messages for a while
        context.bot.restrict_chat_member(chat_id=message.chat_id, user_id=message.from_user.id, permissions=ChatPermissions())
        # Send warning message to the user
        context.bot.send_message(chat_id=message.chat_id, text=f"@{message.from_user.username} you have been warned, abusive language is not allowed.")



def delete_message(update, context):
    """Delete message containing 'pagal' in usernames"""
    message = update.message
    if message and message.from_user and 'pagal' in message.from_user.username.lower():
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        # Restrict the user from sending messages for a while
        context.bot.restrict_chat_member(chat_id=message.chat_id, user_id=message.from_user.id, permissions=ChatPermissions())
        # Send warning message to the user
        context.bot.send_message(chat_id=message.chat_id, text=f"@{message.from_user.username} you have been warned, abusive language is not allowed.")




def delete_message(update, context):
    """Delete message containing 'pagal' in usernames"""
    message = update.message
    if message and message.from_user and 'pagal' in message.from_user.username.lower():
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        # Restrict the user from sending messages for a while
        context.bot.restrict_chat_member(chat_id=message.chat_id, user_id=message.from_user.id, permissions=ChatPermissions())
        # Send warning message to the user
        context.bot.send_message(chat_id=message.chat_id, text=f"@{message.from_user.username} you have been warned, abusive language is not allowed.")


def delete_message(update, context):
    """Delete message containing 'pagal' in usernames"""
    message = update.message
    if message and message.from_user and 'pagal' in message.from_user.username.lower():
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        # Restrict the user from sending messages for a while
        context.bot.restrict_chat_member(chat_id=message.chat_id, user_id=message.from_user.id, permissions=ChatPermissions())
        # Send warning message to the user
        context.bot.send_message(chat_id=message.chat_id, text=f"@{message.from_user.username} you have been warned, abusive language is not allowed.")



def delete_message(update, context):
    """Delete message containing 'pagal' in usernames"""
    message = update.message
    if message and message.from_user and 'pagal' in message.from_user.username.lower():
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        # Restrict the user from sending messages for a while
        context.bot.restrict_chat_member(chat_id=message.chat_id, user_id=message.from_user.id, permissions=ChatPermissions())
        # Send warning message to the user
        context.bot.send_message(chat_id=message.chat_id, text=f"@{message.from_user.username} you have been warned, abusive language is not allowed.")



        





def main():


    """Main function to start the bot."""
    updater = Updater( use_context=True)
    dp = updater.dispatcher

    # Add handler to delete messages containing 'pagal' in usernames
    dp.add_handler(MessageHandler(Filters.all & (~Filters.command), delete_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
