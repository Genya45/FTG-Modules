from .. import loader, utils

def register(cb):
	cb(ArhiopteryxTestMod())

class ArhiopteryxTestMod(loader.Module):
	"""Test Arhiopteryx."""
	strings = {'name': 'ArhiopteryxTest'}
	async def arhiopteryxcmd(self, message):
		"""Использование: .arhiopteryx <текст> или реплей."""
		m_text = utils.get_args_raw(message)
		if not m_text:
			reply = await message.get_reply_message()
			if not reply:
				await utils.answer(message, "Дебил ничего не высрал")
				return
			debil_text = reply.raw_text
		else:
			debil_text = m_text            
		await utils.answer(message, "Дебил высрал: " + debil_text)