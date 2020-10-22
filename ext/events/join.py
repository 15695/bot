from discord.ext import commands
import discord

class Join(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = discord.utils.get(member.guild.channels, name = "general")
		embed = discord.Embed(
			title = "Welcome!",
			description = f"{member.mention} joined the server.",
			color = discord.Color.green()
		)
		embed.set_image(url = "https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif")
		embed.set_footer(text = "We hope you enjoy your stay!")
		await channel.send(embed = embed)

def setup(client):
	client.add_cog(Join(client))
