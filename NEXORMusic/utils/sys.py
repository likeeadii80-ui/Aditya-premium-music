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

import time

import psutil

from NEXORMusic.misc import _boot_
from NEXORMusic.utils.formatters import get_readable_time


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    UP = f"{get_readable_time(bot_uptime)}"
    CPU = f"{psutil.cpu_percent(interval=0.5)}%"
    RAM = f"{psutil.virtual_memory().percent}%"
    DISK = f"{psutil.disk_usage('/').percent}%"
    return UP, CPU, RAM, DISK
