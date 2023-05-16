from pyrogram import Client, filters
from pyrogram.types import Message

# Replace with your bot token
BOT_TOKEN = "6158649870:AAHk_PETDLkYJm5FLf2vYNW16LScwV-m7qY"

# Replace with the channel username
CHANNEL_USERNAME = "himanshugheu"


app = Client("my_bot", bot_token=BOT_TOKEN)


# Handler function for the "/start" command
@app.on_message(filters.command(["start"]))
async def start_handler(client: Client, message: Message):
    # Force user to join the channel first
    if not await client.is_chat_member(chat_id=CHANNEL_USERNAME, user_id=message.chat.id):
        await message.reply_text(f"Please join @{CHANNEL_USERNAME} channel first.")
        return
    
    # Send a welcome message with the chat ID
    await message.reply_text(f"Hi there! Your chat ID is {message.chat.id}.")


# Run the bot
app.run()
