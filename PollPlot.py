#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://static.hikari.gay/pollplot_icon.png
# meta banner: https://mods.hikariatama.ru/badges/pollplot.jpg
# requires: matplotlib
# meta developer: @hikarimods
# scope: hikka_only
# scope: hikka_min 1.2.10

import io

import matplotlib.pyplot as plt
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class PollPlotMod(loader.Module):
    """Visualises polls as plots"""

    strings = {
        "name": "PollPlot",
        "no_reply": "🚫 <b>Reply to a poll is required!</b>",
        "no_answers": "😔 <b>This poll has not answers yet.</b>",
    }

    strings_ru = {
        "no_reply": "🚫 <b>Нужен ответ на опрос!</b>",
        "no_answers": "😔 <b>В этом опросе пока что нет участников.</b>",
        "_cmd_doc_plot": "<reply> - Создать визуализацию опроса",
        "_cls_doc": "Визуализирует опросы в виде графиков",
    }

    async def plotcmd(self, message: Message):
        """<reply> - Create plot from poll"""
        reply = await message.get_reply_message()
        if not reply or not getattr(reply, "poll", False):
            await utils.answer(message, self.strings("no_reply"))
            return

        sizes = [i.voters for i in reply.poll.results.results]

        if not sum(sizes):
            await utils.answer(message, self.strings("no_answers"))
            return

        labels = [
            f"{a.text} [{sizes[i]}] ({round(sizes[i] / sum(sizes) * 100, 1)}%)"
            for i, a in enumerate(reply.poll.poll.answers)
        ]

        explode = [0.05] * len(sizes)
        fig1, ax1 = plt.subplots()
        ax1.pie(
            sizes,
            explode=explode,
            labels=labels,
            textprops={"color": "white", "size": "large"},
        )
        buf = io.BytesIO()
        fig1.patch.set_facecolor("#303841")
        fig1.savefig(buf)
        buf.seek(0)

        await self._client.send_file(message.peer_id, buf.getvalue(), reply_to=reply)

        if message.out:
            await message.delete()
