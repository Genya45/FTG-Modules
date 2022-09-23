from curses.ascii import isdigit
from distutils.file_util import move_file
from .. import loader, utils

import inspect
from ..inline.types import InlineQuery


from aiogram.types import (
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineKeyboardButton,
    InputTextMessageContent,
)

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

		
	async def arhiopteryx2cmd(self, message):
		"""Использование: .arhiopteryx2 <текст> или реплей."""
		m_text = utils.get_args_raw(message)
		if not m_text:
			reply = await message.get_reply_message()
			if not reply:
				userText = -1
			userText = -1
		else:
			userText = int(m_text)          
		#f = ' '.join([x.strings["name"] for x in self.allmodules.modules]) 
		#answerText = f
		module = self.allmodules.modules[userText]
		answerText = self.allmodules.modules[userText].strings["name"]
		reply = answerText + '\n'


		commands = {
			name: func
			for name, func in module.commands.items()
			if await self.allmodules.check_security(message, func)
		}

		for name, fun in commands.items():
			#reply += name + '-' + str(fun) + '\n'
			reply += '<code>.' + name + '</code> ' + utils.escape_html(inspect.getdoc(fun)) + '\n'
			pass
		
		#for name, func in module.commands.items():
		#	reply += '<code>.' + name + '</code> ' + utils.escape_html(inspect.getdoc(fun)) + '\n'
			

		#reply += str(dir(module)) + '\n'

		reply = ''
		for module in self.allmodules.modules:
			reply += module.strings["name"] + "\n"
			reply += utils.escape_html(inspect.getdoc(module)) + "\n"

			commands = {
			name: func
			for name, func in module.commands.items()
			if await self.allmodules.check_security(message, func)
			}
			for name, fun in commands.items():
				#reply += name + '-' + str(fun) + '\n'
				reply += '<code>.' + name + '</code> ' + utils.escape_html(inspect.getdoc(fun)) + '\n'
			
			reply += '------------------------' + '\n'


		await utils.answer(message, reply)




	async def arhiopteryx3cmd(self, message):
		"""Использование: .arhiopteryx3 <текст> или реплей."""
		
		await utils.answer(message, self.allmodules.modules[-1].strings["name"])


	@loader.inline_everyone
	async def arhio_inline_handler(self, query: InlineQuery):
		"lincmd inline version"
		m_text = query.args.split(' ')
		
		if not m_text[0].isdigit() and (m_text) != ['']:
			returnList = []


			for module in self.allmodules.modules:
				commands = {
				name: func
				for name, func in module.commands.items()
				}
				moduleName = module.strings["name"] if module.strings["name"].lower().find(m_text[0].lower()) != -1 else ''
				moduleComm = ''
				
				for name, fun in commands.items():
					moduleComm += ' .'+name if moduleName != '' else ''
					if name.find(m_text[0]) != -1:
						resultTuple = {
						"title": '.'+name,
						"description": utils.escape_html(inspect.getdoc(fun)),
						"message": "."+name,
						}
						returnList.append(resultTuple)

				if moduleName != '':
					resultTuple = {
						"title": moduleName,
						"description": moduleComm,
						"message": ".help "+moduleName,
						}
					returnList.append(resultTuple)

			if len(returnList) >= 50:
				return [{
						"title": 'Error ',
						"description": "Results_too_much",
						"message": ".",
						}]
			if len(returnList) == 0:
				return [{
						"title": 'Error ',
						"description": "Not \n Found",
						"message": ".",
						}]

			return returnList
		

		if len(m_text) < 2:

			if m_text[0] != '':
				currListModules = int(m_text[0])
			else:
				currListModules = 1
			countModules = len(self.allmodules.modules)

			if currListModules > (countModules//50 + 1):
				return [{
					"title": 'Error ',
					"description": "list index out of range",
					"message": ".",
					}]
			
			returnList = []
			resultTuple = {
			"title": str(currListModules) + ' / ' + str(countModules//50 + 1),
			"description": "Page",
			"message": "None",
			}
			returnList.append(resultTuple)

			if currListModules == 1:
				minRange = 0
			else:
				minRange = (50 * (currListModules-1) - 2)

			if currListModules != (countModules//50 + 1):
				maxRange = 50*currListModules - 3
			else:
				minRange = (50 * (currListModules-1) - 3)
				maxRange = len(self.allmodules.modules)
			
			for i in range(minRange, maxRange):			
				module = self.allmodules.modules[i]
				title = str(i) + ' ' + module.strings["name"]
				description = utils.escape_html(inspect.getdoc(module))
				message = module.strings["name"]

				resultTuple = {
				"title": title,
				"description": description,
				"message": message,
				}
				returnList.append(resultTuple)
			
			return returnList
		
		else:
			currModelrIndex = int(m_text[1])

			if currModelrIndex > (len(self.allmodules.modules) - 1):
				return [{
					"title": 'Error ',
					"description": "list index out of range",
					"message": ".",
					}]

			module = self.allmodules.modules[currModelrIndex]
			returnList = []
			resultTuple = {
			"title": module.strings["name"],
			"description": utils.escape_html(inspect.getdoc(module)),
			"message": "None",
			}
			returnList.append(resultTuple)

			commands = {
			name: func
			for name, func in module.commands.items()
			}
			for name, fun in commands.items():
				resultTuple = {
				"title": '.'+name,
				"description": utils.escape_html(inspect.getdoc(fun)),
				"message": "."+name,
				}
				returnList.append(resultTuple)

			return returnList