#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : broadcast-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/broadcast-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6677507920:AAGtZW6-2nAYYE-eVi0mZYBR1m0lqVIVhRY")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "25051009"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "9ff274237f809a2f6ae71f975cc48a3d")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://shadow:xyshadow@cluster0.u9c6bco.mongodb.net/?retryWrites=true&w=majority")

    # Group / channel username of the support chat
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "https://t.me/udhdbsbdbdb")

    # List of admin user ids for special functions(Storing as an array)
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6013992289").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
