from datetime import datetime, timedelta
from discord.ext import commands, tasks
from ..util.database import Member
from asyncio import TimeoutError
from random import choice
import discord

class ChatGames(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.list = [
			"hello world", "mudkip", "something"
		]

	@tasks.loop(seconds = 15)
	async def games(self):
		c = self.client.get_channel(766092797702307870)
		word = choice(self.list)

		fetch = await c.fetch_message(c.last_message_id)
		if fetch is not None:
			difference = fetch.created_at - datetime.now()
			if int(str(difference)[0]) > 0:
				return
		else:
			return

		embed = discord.Embed(
			title = "Chat Games",
			description = f'First one to type "{word}" receives 25 coins.',
			color = discord.Color.blue()
		)

		ctx_msg = await c.send(embed = embed)
		ctx = await self.client.get_context(ctx_msg)

		try:
			msg = await self.client.wait_for("message", check = lambda m: m.content.lower() == word, timeout = 20)
		except TimeoutError:
			await ctx.error("No one won the chat game.", title = "Chat Games", no_footer = True)
		else:
			await ctx.result(f"{msg.author.display_name} won the game.", "Chat Games", no_footer = True, trashable = False, color = discord.Color.blue())
			helper = Member(msg.author)
			helper.add_balance(25)

	@commands.Cog.listener()
	async def on_ready(self):
		pass
		# self.games.start()

def setup(client):
	client.add_cog(ChatGames(client))
