from random import randint, choice
from discord.ext import commands
import discord

class Random(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def random(self, ctx, a : int = 1, b : int = 100):
		result = str(randint(a, b))
		await ctx.result("Your random number is " + result + ".")

	@commands.command(aliases = ["choice"])
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def choose(self, ctx, *, args):
		choices = args.split(",")
		await ctx.result("I choose " + "\"" + choice(choices) + "\".")

	@choose.error
	async def choose_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.error("You must specify something to choose from!")

	@commands.command(aliases = ["compatibility"])
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def ship(self, ctx, one: discord.Member, two: discord.Member = None):
		if two is None:
			two = ctx.author

		percentage = str(randint(0, 100))
		await ctx.result(percentage + "%", title = f"Compatibility of {one.display_name} and {two.display_name}")

	@ship.error
	async def ship_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.error("You must specify two people to ship!")

def setup(client):
	client.add_cog(Random(client))
