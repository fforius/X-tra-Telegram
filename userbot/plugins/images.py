"""Download & Upload Images on Telegram
Syntax: .imgg <Name>"""


from userbot.google_images_download import googleimagesdownload
import os
import shutil
from re import findall
from userbot.utils import admin_cmd


@borg.on(admin_cmd("imgg ?(.*)"))
async def img_sampler(event):
    await event.edit("Processing...")
    query = event.pattern_match.group(1)
    lim = findall(r"lim=\d+", query)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 2
    response = googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory"
    }

    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await borg.send_file(await borg.get_input_entity(event.chat_id), lst)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()
