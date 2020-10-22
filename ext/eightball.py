from discord.ext import commands
import random

class Eightball(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["8ball", "8b"])
	@commands.cooldown(1, 3, commands.BucketType.default)
	async def eightball(self, ctx, *, question):
		responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
		await ctx.result(random.choice(responses), "8 Ball")

def setup(client):
	client.add_cog(Eightball(client))