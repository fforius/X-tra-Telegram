# Port from UniBorg to UBotX by @MoveAngel

import datetime

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from ..help import add_help_item
from userbot import bot
from userbot.events import register


@register(outgoing=True, pattern="^.qu(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("`Reply to any user message.`")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("`Reply to text message`")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("`Reply to actual users message.`")
       return
    await event.edit("`Making a Quote...`")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("`Please unblock @QuotLyBot and try again`")
              return
          if response.text.startswith("Hi!"):
             await event.edit("`Can you kindly disable your forward privacy settings for good?`")
          else: 
             await event.delete()   
             await bot.send_file(event.chat_id, response.message)


add_help_item(
    "quotly",
    "Fun",
    "Enhance yout text to sticker.",
    """
    `.qu`
    """
)
