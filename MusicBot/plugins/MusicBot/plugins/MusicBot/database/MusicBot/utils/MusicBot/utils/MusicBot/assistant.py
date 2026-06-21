from pyrogram import Client
from MusicBot.config import API_ID, API_HASH, STRING_SESSION

assistant = Client(
    "assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)
