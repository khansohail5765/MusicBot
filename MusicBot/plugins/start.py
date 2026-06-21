from pyrogram import filters
from pyrogram.types import Message
from MusicBot.bot import app

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("🎵 Music Bot Online")
