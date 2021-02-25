import asyncio
from pyrogram import Client, filters
from pyrogram.types import InputTextMessageContent, InlineQueryResultArticle, Message, InlineQuery
from urllib.parse import quote


app = Client("testsharebot", api_id=1, api_hash="a", bot_token="a")


@app.on_message(filters.group & filters.text & filters.command("share"))
async def groupmsg(client: app, message: Message):
    if message.reply_to_message:
        await message.reply_text(share_link(message.reply_to_message.text))


@app.on_message(filters.private)
async def privatensg(client: app, message: Message):
    await message.reply_text(share_link(message.text))


@app.on_inline_query()
async def inlineshare(client: app, query: InlineQuery):
    if query.query:
        await query.answer([InlineQueryResultArticle(
            "click to share",
        InputTextMessageContent(share_link(query.query))
        )])


def share_link(text: str) -> str:
    return "https://t.me/share/url?url=" + quote(text)

 
app.run()
