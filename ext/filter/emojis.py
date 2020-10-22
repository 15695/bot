from discord.ext import commands
from emoji import UNICODE_EMOJI
import discord

class EmojiFilter(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.client.user:
			return

		emojis = 0
		for char in message.content:
			if char in UNICODE_EMOJI:
				emojis += 1

		if emojis >= 5:
			await message.delete()
			embed = discord.Embed(
				title = "Filter",
				description = "Please don't spam emojis.",
				color = discord.Color.blue()
			)
			embed.set_footer(text = f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
			await message.channel.send(embed = embed)

def setup(client):
	client.add_cog(EmojiFilter(client))