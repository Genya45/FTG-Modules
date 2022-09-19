# ---------------------------------------------------------------------------------
#  ,_     _          
#  |\_,-~/          
#  / _  _ |    ,--.  🌐 This module was loaded through https://t.me/hikkamods_bot
# (  @  @ )   / ,-'  🔐 Licensed under the GNU AGPLv3.
#  \  _T_/-._( (     
#  /         `. \    ⚠️ Owner of this bot doesn't take responsibility for any
# |         _  \ |   errors caused by this module or this module being non-working
#  \ \ ,  /      |   and doesn't take ownership of any copyrighted material.
#   || |-_\__   /    
#  ((_/`(____,-'     
# ---------------------------------------------------------------------------------
# Name: carbon
# Description: Create beautiful code images
# Author: hikariatama
# Commands:
# .carbon
# ---------------------------------------------------------------------------------

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://img.icons8.com/stickers/500/000000/code.png
# meta banner: https://mods.hikariatama.ru/badges/carbon.jpg
# meta developer: @hikarimods
# scope: hikka_only
# scope: hikka_min 1.2.10

import io
from os import stat

import requests
from telethon.tl.types import Message

from .. import loader, utils

# requires: urllib requests


@loader.tds
class CarbonMod(loader.Module):
    """Create beautiful code images"""

    strings = {
        "name": "Carbon",
        "args": "🚫 <b>No args specified</b>",
        "loading": "🕐 <b>Loading...</b>",
    }

    strings_ru = {
        "args": "🚫 <b>Не указаны аргументы</b>",
        "loading": "🕐 <b>Обработка...</b>",
        "_cls_doc": "Создает симпатичные фотки кода",
        "_cmd_doc_carbon": "<код> - Сделать красивую фотку кода",
    }

    async def carboncmd(self, message: Message):
        """<code> - Create beautiful code image"""
        args = utils.get_args_raw(message)

        try:
            code_from_message = (
                await self._client.download_file(message.media, bytes)
            ).decode("utf-8")
        except Exception:
            code_from_message = ""

        try:
            reply = await message.get_reply_message()
            code_from_reply = (
                await self._client.download_file(reply.media, bytes)
            ).decode("utf-8")
        except Exception:
            code_from_reply = ""

        args = args or code_from_message or code_from_reply

        message = await utils.answer(message, self.strings("loading"))

        doc = io.BytesIO(
            (
                await utils.run_sync(
                    requests.post,
                    "https://carbonara-42.herokuapp.com/api/cook",
                    json={"code": args},
                )
            ).content
        )
        doc.name = "carbonized.jpg"

        await self._client.send_message(
            utils.get_chat_id(message),
            file=doc,
            force_document=(len(args.splitlines()) > 50),
            reply_to=getattr(message, "reply_to_msg_id", None),
        )
        await message.delete()