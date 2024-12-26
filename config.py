"""
Configuration module for the bot status checker.

This module loads environment variables required for the bot to function,
such as bot token, API ID and API HASH.
It also sets up the necessary configuration settings.
"""

from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(getenv("API_ID", "9181844"))
    API_HASH = getenv("API_HASH", "996a3e7194a4f07576fda5c20bb1138b")
    BOT_TOKEN = getenv("BOT_TOKEN", "8160540534:AAF8mZO0c9xkBYKsHRQavE2ap9eq8G3x-ug")
    