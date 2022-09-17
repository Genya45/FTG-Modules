from .. import loader, utils, main
import asyncio

@loader.tds
class EyeOfGodMod(loader.Module):
  strings = {"name": "eog-fork"}
  """eog-fork by @vitalyatroz / Original Module By
  https://t.me/zxcminimalized aka Nikita Xyrix🥰"""
  async def dncmd(self, message):
    """ Отправляет uid в глаз бога
    .dn <reply>"""
    reply = await message.get_reply_message()
    await message.edit("<code>Ваш uid:</code> " + str(reply.from_id))
    try:
      await message.client.send_message(2064606507, "<code>#id</code>" + str(reply.sender.id))
      await asyncio.sleep(2) 
      await asyncio.sleep(3)
      await asyncio.sleep(4)
      messages = await message.client.get_messages('Telegram')
      messages[0].click()
      await asyncio.sleep(5)
      messages2 = await message.client.get_messages(2064606507)
      await message.edit(str(messages2[0].message))
    except Exception as ex:
      await message.edit(str(ex))

  async def dnncmd(self, message,):
    """ Отправляет номер/mail в глаз бога
    .dnn номер/mail"""
    args = utils.get_args_raw(message)
    await message.edit("<code>Ваш номер/mail:</code> " + str(args))
    try:
      await message.client.send_message(2064606507, str(args))
      await asyncio.sleep(2) 
      await asyncio.sleep(3)
      await asyncio.sleep(4)
      messages = await message.client.get_messages('Telegram')
      messages[0].click()
      await asyncio.sleep(5)
      messages2 = await message.client.get_messages(2064606507)
      await message.edit(str(messages2[0].message))
    except Exception as ex:
      await message.edit(str(ex))