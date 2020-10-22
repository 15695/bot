from discord.ext import commands
import discord
import asyncio
import random

class Text(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(manage_messages = True)
	async def say(self, ctx, *, message):
		await ctx.message.delete()
		await ctx.result(message, "Say", no_footer = True)

	@commands.command()
	async def clap(self, ctx, *, message):
		await ctx.result(" :clap: ".join(message.split()), "Clapped Message")

	@commands.command()
	async def space(self, ctx, *, message):
		await ctx.result(" ".join(list(message)), "Spaced Message")

	@commands.command()
	async def mock(self, ctx, *, message):
		case = False
		result = []

		for c in message:
			if not case:
				result.append(c.lower())
			else:
				result.append(c.upper())
			case = not case

		await ctx.result("".join(result), "Mock")

	@commands.command()
	async def asked(self, ctx):
		gifs = [
			"https://tenor.com/view/bean-dance-crazy-aye-dats-fr-crazy-hoe-now-show-me-one-person-who-asked-gif-16195074",
			"https://tenor.com/view/who-tf-asked-nasas-radar-dish-who-asked-nobody-asked-gif-17675657",
			"https://tenor.com/view/damn-thats-crazy-who-asked-though-spongebob-dancing-weird-gif-17659544"
		]
		embed = discord.Embed(
			title = "Result",
			color = discord.Color.green()
		)
		embed.set_image(url = random.choice(gifs))
		await ctx.send(embed = embed)

def setup(client):
	client.add_cog(Text(client))