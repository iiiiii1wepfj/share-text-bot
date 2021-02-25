import asyncio
from pyrogram import Client, filters
from pyrogram.types import InputTextMessageContent, InlineQueryResultArticle, Message, InlineQuery
import urllib.parse

api_id = api id
api_hash = 'api hash'
token = "bot token"



app = Client("testsharebot", api_id, api_hash, bot_token=token)


@app.on_message(filters.group & filters.text & filters.command("share"))
async def groupmsg(client: app, message: Message):
 if message.reply_to_message:
  await message.reply_text("https://t.me/share/url?url="+urllib.parse.quote(message.reply_to_message.text))
 else:
  await message.reply_text("https://t.me/share/url?url="+urllib.parse.quote(message.text.split(None, 1)[1]))



@app.on_message(filters.private)
async def privatensg(client: app, message: Message):
    await message.reply_text("https://t.me/share/url?url="+urllib.parse.quote(message.text))




@app.on_inline_query()
async def inlineshare(client: app, query: InlineQuery):
    if query.query != "":
     await query.answer([InlineQueryResultArticle(
         "click to share",
        InputTextMessageContent("https://t.me/share/url?url="+urllib.parse.quote(query.query))
      )])


     

        
app.run()
