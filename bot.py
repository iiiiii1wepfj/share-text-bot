from urllib.parse import quote

from pyrogram import Client, filters
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, Message


api_id = api id
api_hash = 'api hash'
token = "bot token"



app = Client("testsharebot", api_id, api_hash, bot_token=token)

@app.on_message(filters.group & filters.text & filters.command("share"))
async def groupmsg(client: app, message: Message):
    replied = message.reply_to_message
    await message.reply_text(
        share_link(replied.text if replied else message.text.split(None, 1)[1])
    )


@app.on_message(filters.private)
async def privatensg(client: app, message: Message):
    await message.reply_text(share_link(message.text))


@app.on_inline_query()
async def inlineshare(client: app, query: InlineQuery):
    if query.query:
        await query.answer(
            [
                InlineQueryResultArticle(
                    "click to share", InputTextMessageContent(share_link(query.query))
                )
            ]
        )


def share_link(text: str) -> str:
    return "https://t.me/share/url?url=" + quote(text)


app.run()
