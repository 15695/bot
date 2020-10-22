from discord.ext import commands
import discord

class Clear(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(manage_channels = True)
	@commands.bot_has_permissions(manage_channels = True)
	@commands.guild_only()
	async def nuke(self, ctx):
		"""Easily clear the entire channel."""
		channel = await ctx.channel.clone()
		await ctx.channel.delete()

		msg = await channel.send("Loading...")
		ctx = await self.client.get_context(msg)
		await msg.delete()

		await ctx.result("Nuked the channel. https://media.giphy.com/media/oe33xf3B50fsc/giphy.gif")

	@commands.command()
	@commands.has_permissions(manage_messages = True)
	@commands.bot_has_permissions(manage_messages = True)
	@commands.guild_only()
	async def clear(self, ctx, limit: int, author: discord.Member = None):
		"""Delete a specified amount of messages."""
		def check(message):
			if author is None:
				return True
			return message.author == author

		await ctx.channel.purge(limit = limit + 1, check = check)

def setup(client):
	client.add_cog(Clear(client))
