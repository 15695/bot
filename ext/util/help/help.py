from discord.ext.commands import HelpCommand
import discord

class CustomHelpCommand(HelpCommand):
	async def send_bot_help(self, mapping):
		prefix = await self.context.bot.get_prefix(self.context.message)
		embed = discord.Embed(
			title = "Help",
			description = f"You can use {prefix}help to get more info on a command or category.",
			color = discord.Color.blue()
		)
		embed.add_field(name = "Categories", value = "insert categories here")
		await self.context.send(embed = embed)

	async def send_command_help(self, command):
		embed = discord.Embed(
			title = "Help",
			description = f"Showing help on the command `{command.name}`.",
			color = discord.Color.blue()
		)
		embed.add_field(name = "Usage", value = "insert usage here")

		if len(command.aliases) == 0:
			aliases = "None"
		else:
			aliases = ", ".join(command.aliases)

		embed.add_field(name = "Aliases", value = aliases, inline = False)
		await self.context.send(embed = embed)
