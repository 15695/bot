from discord.ext import commands

class SubredditConverter(commands.Converter):
	async def convert(self, ctx, argument):
		if argument.startswith("r/"):
			argument = argument[2:]

		return argument

class Reddit(commands.Cog):
	def __init__(self, client):
		self.client = client

	# @commands.command(aliases = ["reddit"])
	# async def subreddit(self, ctx, subreddit: SubredditConverter, sort, *, flair):
	# 	pass
	#
	# @commands.command(aliases = ["memes"])
	# async def meme(self, ctx):
	# 	await self.subreddit(ctx, "memes", "hot")

def setup(client):
	client.add_cog(Reddit(client))