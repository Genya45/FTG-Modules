"""
    ____  __  __ _                            __ _   _  _   _           _     _
   / __ \|  \/  (_)_ __   ___  ___ _ __ __ _ / _| |_| || | | |__   __ _| |__ (_) ___  ___
  / / _` | |\/| | | '_ \ / _ \/ __| '__/ _` | |_| __| || |_| '_ \ / _` | '_ \| |/ _ \/ __|
 | | (_| | |  | | | | | |  __/ (__| | | (_| |  _| |_|__   _| |_) | (_| | |_) | |  __/\__ \
  \ \__,_|_|  |_|_|_| |_|\___|\___|_|  \__,_|_|  \__|  |_| |_.__/ \__,_|_.__/|_|\___||___/
   \____/
"""
import io
import datetime
import requests
import random
from telethon.sync import TelegramClient
from telethon import functions
from .. import loader, utils

def date():
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    return date

def register(cb):
    cb(minusrus_mc4b1Mod())

class minusrus_mc4b1Mod(loader.Module):
    """Как там дела у солдатиков?"""
    strings = {
        'name': 'MinusRus',
        'loading_minusrus'  : '<b>Считаем ручки и ножки...</b>',
        'loading_deadrus'   : '<b>Ищем по кустикам...</b>',
        'caption_minusrus'  : '<b>Данные от ВСУ на <u>{}</u>.</b>',
        'caption_deadrus'   : '<b>Один(ни) из <u>{}</u> запечатлённых мёртвых солдат армии РФ.</b>',
    }

    def __init__(self):
        self.name = self.strings['name']

    @loader.unrestricted
    async def deadruscmd(self, message):
        """.deadrus <"snore", "eblo" или ничего> чтобы получить случайных мёртвых солдатиков))"""

        channel_with_corpses = '@russian_corpses_are_in_ukraine'
        await message.edit(self.strings['loading_deadrus'])
        reply = await message.get_reply_message()

        amount_of_dead_rus = (await message.client.get_messages(channel_with_corpses, limit=0)).total
        last_dead_rus = (await message.client.get_messages(channel_with_corpses, limit=1, reverse=False))[0].id
        while True:
            deadrusid = random.randint(1, last_dead_rus)
            randomdeadrus = await message.client.get_messages(channel_with_corpses, ids=deadrusid)
            try:
                if message.out:
                    await message.delete()
                    await message.client.send_file(message.chat_id, file=randomdeadrus.media,
                                                   caption=self.strings['caption_deadrus'].format(amount_of_dead_rus), reply_to=reply)
                else:
                    if reply:
                        await message.client.send_file(message.chat_id, file=randomdeadrus.media,
                                                       caption=self.strings['caption_deadrus'].format(amount_of_dead_rus), reply_to=reply)
                    else:
                        await message.client.send_file(message.chat_id, file=randomdeadrus.media,
                                                       caption=self.strings['caption_deadrus'].format(amount_of_dead_rus), reply_to=message)
                break
            except:
                None
        if utils.get_args_raw(message) == 'snore':
            voice = (await message.client.get_messages('@mc4b_files_for_modules', search='MinusRus: snore'))[0]
            await message.client.send_file(message.chat_id, voice.media, reply_to=(await message.client.get_messages(message.chat_id, limit=1, reverse=False))[0])
        elif utils.get_args_raw(message) == 'eblo':
            voice = (await message.client.get_messages('@mc4b_files_for_modules', search='MinusRus: eblo'))[0]
            await message.client.send_file(message.chat_id, voice.media, reply_to=(await message.client.get_messages(message.chat_id, limit=1, reverse=False))[0])


    @loader.unrestricted
    async def minusruscmd(self, message):
        """Чтобы узнать  потери РФ по оценке ВСУ.


        👨‍💻Made by: @Minecraft4babies_GFTG_Modules"""

        await message.edit(self.strings['loading_minusrus'])
        reply = await message.get_reply_message()

        preview = await message.client(functions.messages.GetWebPagePreviewRequest('https://minusrus.com/ru'))

        if message.out:
            await message.delete()
            await message.client.send_file(message.chat_id, file=preview.webpage.photo,
                                           caption=self.strings['caption_minusrus'].format(date()), reply_to=reply)
        else:
            await message.client.send_file(message.chat_id, file=preview.webpage.photo,
                                           caption=self.strings['caption_minusrus'].format(date()), reply_to=message)
