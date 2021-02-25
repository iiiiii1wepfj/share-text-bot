from urllib.parse import quote
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InputTextMessageContent, InlineQueryResultArticle, Message, InlineQuery	

api_id = api id
api_hash = 'api hash'
token = "bot token"



app = Client(':memory:', api_id, api_hash, bot_token=token)

@app.on_message(filters.group & filters.text & filters.command("share"))
async def groupmsg(client: app, message: Message):
    reply = message.reply_to_message
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text("**ERROR** : `No Input found !`")
        await asyncio.sleep(10)
        await message.delete()
        return
    await message.reply_text(share_link(input_text))


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
