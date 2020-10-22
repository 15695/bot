from discord.ext import commands
from ..util.database import Member
import discord

class Basic(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["bal"])
	async def balance(self, ctx, member: discord.Member = None):
		if member is None:
			member = ctx.author
		await ctx.result(str(Member(member).balance) + " coins", title = "Balance")

	@commands.command()
	async def pay(self, ctx, members: commands.Greedy[discord.Member], amount: int):
		for member in members:
			helper = Member(member)
			helper2 = Member(ctx.author)

			helper.add_balance(amount)
			helper2.subtract_balance(amount)

		await ctx.result(f"You paid {', '.join([m.name for m in members])} {amount} coins.")

	@commands.is_owner()
	@commands.command()
	async def yoink(self, ctx, member: discord.Member, amount: int):
		helper = Member(member)
		helper2 = Member(ctx.author)

		helper.subtract_balance(amount)
		helper2.add_balance(amount)

		await ctx.result(f"You yoinked {amount} coins from {member}.")

def setup(client):
	client.add_cog(Basic(client))