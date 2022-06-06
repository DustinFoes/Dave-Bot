import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio



class errors(commands.Cog):

	def __init__(self, client):
		self.client = client
	


	client = commands.Bot(command_prefix = '!')

	@commands.Cog.listener()
	async def on_message(self, message):
		if "AssertionError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="AssertionError!",
				value="	Raised when the assert statement fails.",
			)
			await message.channel.send(embed=em)

		elif "AttributeError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="AttributeError!",
				value="Raised on the attribute assignment or reference fails.",
			)
			await message.channel.send(embed=em)

def setup(client):
	client.add_cog(errors(errors))