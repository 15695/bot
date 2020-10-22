from discord.ext import commands
import discord

class FilesFilter(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.client.user:
			return

		for a in message.attachments:
			ext = a.filename.split(".")
			if not len(ext) > 1:
				await message.delete()
				embed = discord.Embed(
					title = "Filter",
					description = "Sorry, for safety reasons, we don't currently allow users to post files without a known file extension. Please rename this file and send it again.",
					color = discord.Color.blue()
				)
				embed.set_footer(text = f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
				await message.channel.send(embed = embed)

def setup(client):
	client.add_cog(FilesFilter(client))