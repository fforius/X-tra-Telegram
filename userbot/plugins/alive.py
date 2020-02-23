"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`POCO BOT IS ACTIVATED! ψ(｀∇´)ψ`**\n\n"
                     "`Telethon version: 3.1.3\nPython: 2.1.2 Kapak Merah`\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     f"`My owner`: {DEFAULTUSER}\n"
                      f"`============================`\n"
                     f"  ⠀⡷⣾⣎⣷⡗⣿⣾⠑⣇⣿⣾⣉⢾⡑⣿⠒⣾⣉⣿⡱⠀\n" 
                     f"⠀  ⠃⠛⠃⠛⠃⠛⠙⠊⠃⠛⠛⠒⠑⠋⠙⠊⠛⠒⠛⠑⠀\n"
                     f"⣿⣿⣿⣿⣿⣿⣿⣿⠿⠻⠿⡿⠿⠻⠿⡿⠿⠻⠿⣿⣿⣿⣿⣿\n"
                     f"⣿⣿⣿⣿⣿⡿⠋⣼⠀⠀⠀⡇⠀⠀⠀⡇⠀⠀⠀⣿⣿⣿⣿⣿\n"
                     f"⣿⣿⣿⣿⡉⠒⠤⠿⠶⠀⠶⠷⠶⠀⠶⠷⠶⠀⠶⢿⣿⣿⣿⣿\n"
                     f"⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿\n"
                     f"⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⡛⠛⠛⢛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿\n"
                     f"⣿⠀⠀⠀⠀⠀⣠⠀⢤⣼⣿⣤⣤⣿⣧⡤⣠⡀⣠⡀⣠⡀⠀⣿\n"
                     f"⣿⠀⣀⠀⣼⣿⣿⡆⠀⢻⣏⣻⣟⣹⡟⠀⣿⡏⣿⡏⣿⡏⠀⣿\n"
                     f"⣿⠀⠙⣿⡿⠿⢿⣿⣄⡀⣿⣿⣿⣿⠀⠀⣿⣧⣿⣧⣿⡇⠀⣿\n"
                     f"⣿⠀⠀⠋⠀⢴⣿⣿⡟⣴⣿⣷⣾⣿⣷⠄⠉⠉⣿⡏⠉⠁⠀⣿\n"
                     f"⣿⠀⠀⠀⠀⠀⣿⣿⠀⢿⣿⣿⣿⣿⣥⣴⣾⣿⣿⣷⠀⠀⠀⣿\n"
                     f"⣿⠀⠀⠀⠀⠀⣿⣿⠀⣠⣿⣿⣿⣿⣿⣷⣤⣀⣿⣿⠀⠀⠀⣿\n"
                     f"⣿⠀⠀⠀⠀⠀⣿⣿⣷⣿⣿⣿⣿⣿⠋⠙⠻⢿⣿⡟⠀⠀⠀⣿\n"
                     f"⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣾⡗⠀⠀⣿⡇⠀⠀⠀⣿\n"
                     f"⣿⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⢻⣿⣿⣷⣶⡄⣿⡇⠀⠀⠀⣿\n"
                     f"⠙⢷⣄⠀⠀⠀⠀⠀⠀⣿⣿⣿⣄⠙⣿⣿⣿⡇⣿⡇⠀⣠⡾⠋\n"
                     f"⠀⠀⠙⢷⣄⠀⠀⠀⠀⣿⣿⣿⠟⠀⠀⠻⣿⡇⡿⣡⡾⠋⠀⠀\n"
                     f"⠀⠀⠀⠀⠙⢷⣄⠀⠀⢻⣿⣿⣄⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀\n"
                     f"⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⣿⣿⣿⠆⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀\n"
                     f"⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣝⠋⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀\n"
                     f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
                     f"⠀⠀⠀⠀⡄⣤⠀⣄⣤⠀⣤⠀⣤⣀⠀⣠⠤⠀⣤⢄⠀⠀⠀⠀\n"
                     f"⠀⠀⠀⠀⢇⡿⠀⡇⣿⠀⣿⠀⢿⡠⠀⣿⣉⠀⣿⡸⠀\n"
                     f"`============================`\n"
                     f"**Poco Poco** ❣️...\n"
                     f"`============================`"
                    )
