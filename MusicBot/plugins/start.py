from pyrogram import filters
from pyrogram.types import Message
from MusicBot.bot import app

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("🎵 Music Bot Online")

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(filters.command("start"))
async def start(_, message):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➕ Add Me", url="https://t.me/YourBot?startgroup=true")
            ],
            [
                InlineKeyboardButton("📚 Commands", callback_data="help"),
                InlineKeyboardButton("👤 Owner", url="https://t.me/YourUsername")
            ]
        ]
    )

    await message.reply_photo(
        photo="https://example.com/musicbot.jpg",
        caption="🎵 Welcome To Music Bot",
        reply_markup=buttons
    )
