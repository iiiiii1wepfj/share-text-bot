from urllib.parse import quote

from pyrogram import Client, filters
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

app = Client("testsharebot", api_id=1, api_hash="a", bot_token="a")


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
