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

# Re-export from root all_platforms.py
try:
    from all_platforms import API_KEY, API_URL, DEFAULT_API_KEY, DEFAULT_API_URL
except Exception:
    import os
    API_URL = (
        os.getenv("API_URL")
        or os.getenv("NEXOR_API_URL")
        or os.getenv("RITESH_API_URL")
        or "https://api.riteshyt.in"
    ).rstrip("/")
    API_KEY = (
        os.getenv("API_KEY")
        or os.getenv("NEXOR_API_KEY")
        or os.getenv("RITESH_API_KEY")
        or "riteshfree7bf33e2c0825084d93617e83"
    )
    DEFAULT_API_URL = API_URL
    DEFAULT_API_KEY = API_KEY

__all__ = ["API_URL", "API_KEY", "DEFAULT_API_URL", "DEFAULT_API_KEY"]
