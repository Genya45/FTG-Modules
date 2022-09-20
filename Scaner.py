from .. import loader, utils, main
import asyncio

@loader.tds
class ScanerMod(loader.Module):
  strings = {"name": "Scaner"}
  """Scaner by @vitalyatroz"""
  async def scancmd(self, message):
    """ Сканує текст на фото """
    reply = await message.get_reply_message()
    await message.edit("<code>Зачекайте...</code>")
    try:
      await message.client.send_file(1143553797, reply.media)
      await asyncio.sleep(2) 
      messages = await message.client.get_messages('Telegram')
      messages[0].click()
      await asyncio.sleep(2)
      messages2 = await message.client.get_messages(1143553797, limit=2)
      await message.edit(str(messages2[1].message))
    except Exception as ex:
      await message.edit(str(ex))