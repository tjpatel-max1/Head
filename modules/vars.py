# 🇳 🇮 🇰 🇭 🇮 🇱

import os
from os import environ


# ======================
# BASIC CONFIG
# ======================

API_ID = int(environ.get("API_ID", 0))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", 0))
CREDIT = environ.get("CREDIT", "Admin")

cookies_file_path = os.getenv(
    "cookies_file_path",
    "youtube_cookies.txt"
)


# ======================
# USERS SAFE PARSER
# ======================

def parse_users(env_name):
    raw = environ.get(env_name, "")
    return [
        int(x.strip())
        for x in raw.split(",")
        if x.strip().isdigit()
    ]


TOTAL_USERS = parse_users("TOTAL_USERS")
AUTH_USERS = parse_users("AUTH_USERS")


# Always allow owner
if OWNER and OWNER not in AUTH_USERS:
    AUTH_USERS.append(OWNER)


# ======================
# API CONFIG
# ======================

api_url = "http://master-api-v3.vercel.app/"
api_token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"

