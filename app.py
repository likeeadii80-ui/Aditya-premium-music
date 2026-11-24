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

import sys

print("🚀 Starting NEXORMusic Bot...")

try:
    # Run the package as module
    import runpy

    runpy.run_module("NEXORMusic", run_name="__main__")
except Exception as e:
    print("❌ Bot crashed with error:", e)
    sys.exit(1)
