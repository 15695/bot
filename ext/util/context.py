from discord.ext import commands
from discord import Color, Embed
from asyncio import TimeoutError
import datetime

class CustomContext(commands.Context):
	"""Subclassed for additional functionality."""

	async def error(self, info, *, title = "Error", trashable = True, no_footer = False):
		await self.result(info, title, trashable = trashable, no_footer = no_footer, color = Color.red())

	async def result(self, message = "", title = "Result", *, trashable = True, no_footer = False, color = Color.green()):
		embed = Embed(
			title = title,
			description = message,
			color = color
		)

		embed.timestamp = datetime.datetime.now()

		text = self.author.name + "#" + self.author.discriminator
		if not no_footer:
			embed.set_footer(text = text, icon_url = self.author.avatar_url)

		msg = await self.send(embed = embed)

		if not trashable:
			return

		await msg.add_reaction("🗑️")

		def check(r, u):
			if str(r.emoji) == "🗑️" and u.id in [self.author.id] and r.message == msg:
				return True
			if not u.bot:
				self.bot.loop.create_task(r.remove(u))

		try:
			await self.bot.wait_for("reaction_add", check = check, timeout = 120)
		except TimeoutError:
			await msg.clear_reactions()
		else:
			await msg.delete()

	async def ok(self):
		await self.message.add_reaction("✅")