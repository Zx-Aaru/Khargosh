from datetime import datetime
import random
from pyrogram import filters
from pyrogram.types import Message, InputMediaPhoto

from AarumiMusic import app
from AarumiMusic.core.call import Aarumi
from AarumiMusic.utils import bot_sys_stats
from AarumiMusic.utils.decorators.language import language
from AarumiMusic.utils.inline import supp_markup
from config import BANNED_USERS


PING_IMAGES = [
    "https://files.catbox.moe/fh7vw7.jpg",
    "https://files.catbox.moe/lckxh6.jpg",
    "https://files.catbox.moe/smteo6.jpg",
    "https://files.catbox.moe/7enu2i.jpg",
    "https://files.catbox.moe/n6hkvd.jpg",
    "https://files.catbox.moe/ej1p7t.jpg",
]


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()

    # spoiler image 
    first_image = random.choice(PING_IMAGES)
    response = await message.reply_photo(
        photo=first_image,
        caption=_["ping_1"].format(app.mention),
        has_spoiler=True
    )

    # Stats
    pytgping = await Aarumi.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    # नया image (random) + caption
    new_image = random.choice(PING_IMAGES)
    await response.edit_media(
        InputMediaPhoto(
            media=new_image,
            caption=_["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        ),
        reply_markup=supp_markup(_),
    )
