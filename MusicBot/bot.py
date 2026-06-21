from pyrogram import Client
from MusicBot.config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def start(_, message):
    if message.text == "/start":
        await message.reply_text("🎵 Music Bot Online")

app.run()
