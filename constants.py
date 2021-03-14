from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_message_text = """Hello {}, this is a bot to share text. created by @tdicprojects"""

start_message_reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(  
                        "Inline here 🔍",
                        switch_inline_query_current_chat=""
                    )
        ],
        [
            InlineKeyboardButton("🆘 Help",  callback_data="help"),
        ],
        [
            InlineKeyboardButton(
                "source code",  url="https://github.com/iiiiii1wepfj/share-text-bot"),
        ],
        [
            InlineKeyboardButton(
                "📣 Channel",  url="https://t.me/TDICProjects"),
            InlineKeyboardButton(
                "Group 👥",  url="https://t.me/TDICSupport"),
        ]
    ]
)

error_message_text = """**ERROR** : `No Input found !`"""

error_message_reply_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton("delete this message", "deleterrormessage")]]
            )

inline_share_message_text = """click to share"""

help_text = """ **share text bot**
i am a bot to create a link to share text in the telegram.
****help****
**Groups**
/share (text or reply to message)
**private chat**
(text)
**inline mode**
@TDICShareBot (text)
"""

help_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Back", callback_data="back")],
            ]
        )
