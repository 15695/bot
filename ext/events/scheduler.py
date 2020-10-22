# from ..util.scheduler import Scheduler
from discord.ext import commands

class SchedulerCog(commands.Cog):
	def __init__(self, client):
		self.client = client
		# self.scheduler = Scheduler()

def setup(client):
	pass
	# client.add_cog(SchedulerCog(client))