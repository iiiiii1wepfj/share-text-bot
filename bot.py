from urllib.parse import quote
from config import API_ID, API_HASH, TOKEN, sudofilter
from pyrogram import Client, filters
from pyrogram.types import (
    InputTextMessageContent,
    InlineQueryResultArticle,
    Message,
    InlineQuery,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import os, sys
from threading import Thread

app = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN)

def stop_and_restart():
    app.stop()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, *sys.argv)


@app.on_message(filters.command("r") & sudofilter & ~filters.forwarded & ~filters.group & ~filters.edited & ~filters.via_bot)
async def restart(app, message):
    Thread(
        target=stop_and_restart
    ).start()

@app.on_message(filters.command("start") & filters.private)
async def start(client: app, message: Message):
    await message.reply_text(f"Hello {message.from_user.mention()}, this is a bot to share text. created by @tdicprojects", reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(  
                        "Inline here 🔍",
                        switch_inline_query_current_chat=""
                    )
        ],
        [
            InlineKeyboardButton(
                "📣 Channel",  url="https://t.me/TDICProjects"),
            InlineKeyboardButton(
                "Group 👥",  url="https://t.me/TDICSupport"),
        ]
    ]
))

@app.on_message(filters.group & filters.text & filters.command("share"))
async def groupmsg(client: app, message: Message):
    reply = message.reply_to_message
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            "**ERROR** : `No Input found !`",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("delete this message", "deleterrormessage")]]
            ),
        )
        return
    await message.reply_text(share_link(input_text))


@app.on_callback_query(filters.regex("^deleterrormessage"))
async def delerrmsg(client: app, cquery: CallbackQuery):
    await cquery.message.delete()


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
