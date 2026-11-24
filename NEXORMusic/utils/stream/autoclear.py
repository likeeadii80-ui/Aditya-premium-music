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

import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass
