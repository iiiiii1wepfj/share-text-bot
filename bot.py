from urllib.parse import quote
from config import API_ID, API_HASH, TOKEN, sudofilter
from hydrogram import Client, filters
from hydrogram.types import (
    InputTextMessageContent,
    InlineQueryResultArticle,
    Message,
    InlineQuery,
    CallbackQuery,
)
import os, sys
from threading import Thread
import constants

app = Client(
    "sharetextbot", in_memory=True, api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN
)


def stop_and_restart():
    app.stop()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, *sys.argv)


@app.on_callback_query(filters.regex(r"^back"))
async def backtostart(client: app, cquery: CallbackQuery):
    await cquery.message.edit(
        constants.start_message_text.format(cquery.from_user.mention()),
        reply_markup=constants.start_message_reply_markup,
    )


@app.on_callback_query(filters.regex(r"^help"))
async def helpbutton(client: app, cquery: CallbackQuery):
    await cquery.message.edit(constants.help_text, reply_markup=constants.help_markup)


@app.on_message(
    filters.command("r")
    & sudofilter
    & ~filters.forwarded
    & ~filters.group
    & ~filters.via_bot
)
async def restart(app, message):
    Thread(target=stop_and_restart).start()


@app.on_message(filters.command("start") & filters.private)
async def start(client: app, message: Message):
    if len(message.text.split()) > 1:
        if message.command[1] == "help":
            await message.reply_text(constants.help_text)
    else:
        await message.reply_text(
            constants.start_message_text.format(message.from_user.mention()),
            reply_markup=constants.start_message_reply_markup,
        )


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
            constants.error_message_text,
            reply_markup=constants.error_message_reply_markup,
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
                    constants.inline_share_message_text,
                    InputTextMessageContent(share_link(query.query)),
                )
            ]
        )


def share_link(text: str) -> str:
    return "https://t.me/share/url?url=" + quote(text)


app.run()
