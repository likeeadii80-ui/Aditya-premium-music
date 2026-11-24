# ─────────────────────────────────────────────────────────────
# NEXOR MUSIC  —  Developed & maintained by ADITYA
# Developer : https://t.me/NEXOR_BLAZE
# Channel   : https://t.me/MUSIXX_HUB

# Copyright (C) 2026 by Aditya (NEXOR_BLAZE)@Telegram, < https://t.me/NEXOR_BLAZE >.
# This file is part of < https://t.me/MUSIXX_HUB > project (NEXOR MUSIC),
# modified from AloneMusic and released under the "GNU v3.0 License Agreement".
# Please see the LICENSE file included with this project.
#
# All rights reserved.

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from NEXORMusic import app
from NEXORMusic.core.call import NEXOR
from NEXORMusic.utils import bot_sys_stats
from NEXORMusic.utils.decorators.language import language
from NEXORMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await NEXOR.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
