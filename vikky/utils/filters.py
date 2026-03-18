from pyrogram import filters
from config import OWNER_ID
from vikky.core.sudo import SUDO_USERS
from vikky.core.bot import MASTER_OWNER

def owner_filter(_, __, message):
    return message.from_user and (
        message.from_user.id == OWNER_ID or
        message.from_user.id == MASTER_OWNER
    )

def sudo_filter(_, __, message):
    return message.from_user and message.from_user.id in SUDO_USERS

owner = filters.create(owner_filter)
sudo = filters.create(sudo_filter)

owner_or_sudo = owner | sudo
