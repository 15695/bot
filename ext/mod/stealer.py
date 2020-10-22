from discord.ext import commands
import discord
import aiohttp

class EmojiStealer(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def steal(self, ctx, id, name):
		url = "https://cdn.discordapp.com/emojis/" + id
		emoji = None

		async with aiohttp.ClientSession() as session:
			async with session.get(url) as response:
				emoji = await response.read()
		
		await ctx.guild.create_custom_emoji(
			name = name,
			image = emoji,
			reason = "Emoji Stealer"
		)


def setup(client):
	client.add_cog(EmojiStealer(client))