from pyrogram import Client

api_id = "28017104"
api_hash = "3b533fc9fae83b8e08a4dfd96830c25b"
bot_token = "6158649870:AAHk_PETDLkYJm5FLf2vYNW16LScwV-m7qY"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
