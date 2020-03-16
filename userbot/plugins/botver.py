""" Userbot module for getting information about the server. """

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.botver$")
async def bot_ver(event):
    """ For .botver command, get the bot version. """
    if which("git") is not None:
        invokever = "git describe --all --long"
        ver = await asyncrunapp(
            invokever,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        invokerev = "git rev-list --all --count"
        rev = await asyncrunapp(
            invokerev,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await rev.communicate()
        revout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        await event.edit("`Userbot Version: "
                         f"{verout}"
                         "` \n"
                         "`Revision: "
                         f"{revout}"
                         "`")
    else:
        await event.edit(
            "Shame that you don't have git, You're running 5.0 - 'Extended' anyway"
        )

        CMD_HELP.update({"botver": ".botver\
            \nUsage: Shows the userbot version."})
