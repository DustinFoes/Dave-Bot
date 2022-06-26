import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand

# ///-------------------------------------------------------------------------------------\\\

'''Simple Bot That Listens for People That ask Simple / Common Questions relating to discord.py, Then Displays Information and a link to a website that provides information or help for the given issue.'''


class discord_py_errors(commands.Cog):

	def __init__(self, client):
		self.client = client


	client = commands.Bot(command_prefix = '')
	slash = SlashCommand(client, sync_commands=True)




# /// DISCORD.PY_ERRORS \\\



	@commands.Cog.listener()
	async def on_message(self, message):
		if "indentation error" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", 
				description="", 
				color=0x22FC00
			)
			em.add_field(
				name="Indentation Error",
				descrption="This is usually due to use of inconstant tabs and spaces. Note: Lately people have noticed when copy pasting code from the internet, this will insert the code with the opposite indentation that is of the current file.",
				color=0x22FC00,
			)
			await message.channel.send(embed=em)
	
		elif "application did not respond" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", 
				description="", 
				color=0x22FC00
			)
			em.add_field(
				name="the application did not respond",
				description="If your bot does not respond to an interaction within 3 seconds, the interaction will fail (although not necessarily an error has occured in your application). You can defer if you know it will take longer time.",
				url='https://stackoverflow.com/questions/70996186/the-application-did-not-respond-error-while-making-a-slash-command-using-disco#:~:text=If%20your%20bot%20does%20not%20respond%20to%20an%20interaction%20within%203%20seconds%2C%20the%20interaction%20will%20fail%20(although%20not%20necessarily%20an%20error%20has%20occured%20in%20your%20application).%20You%20can%20defer%20if%20you%20know%20it%20will%20take%20longer%20time.',
			)
			await message.channel.send(embed=em)
	
		elif "spaces in an argument" in message.content:
			em = discord.Embed(
				title="Coding Error Detection",  
				color=0x22FC00,
			)
			em.add_field(
				name="spaces in an argument",
				description="	Raised when the assert statement fails.",
				url="https://stackoverflow.com/questions/56006198/is-there-a-way-to-include-spaces-in-my-argument?rq=1#:~:text=You%20have%20a%20few%20options%3A",
			)
			await message.channel.send(embed=em)
	
		elif "bot cant see members" in message.content:
			em = discord.Embed(
				title="Coding Error Detection",
				color=0x22FC00
			)
			em.add_field(
				name="How to Fix: Bot Cant See Errors",
				url="https://stackoverflow.com/questions/64231025/discord-py-bot-cant-see-members",
			)
			await message.channel.send(embed=em)
	
		elif "argument 'deny_new'" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", 
				description="", 
				color=0x22FC00
			)
			em.add_field(
				name="deny_new",
				description="How to Fix: deny_new",
				url="https://stackoverflow.com/questions/63027848/discord-py-error-typeerror-new-got-an-unexpected-keyword-argument-deny"
			)
			await message.channel.send(embed=em)
	
		elif "invalid syntax with async def" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", 
				description="", 
				color=0x22FC00
			)
			em.add_field(
				name="How to Fix: Invalid Syntax With Async Def",
				url="https://stackoverflow.com/questions/43948454/python-invalid-syntax-with-async-def",
			)
			await message.channel.send(embed=em)
	
		elif "on_message stops commands from working" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", 
				description="", 
				color=0x22FC00
			)
			em.add_field(
				name="How to Fix: on_message Stops Commands From Working",
				description="",
			)
			await message.channel.send(embed=em)
	
		elif "how to send an embed" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", 
				description="", 
				color=0x22FC00
			)
			em.add_field(
				name="How To Send an Embed",
				description="",
				url="https://stackoverflow.com/questions/44862112/how-can-i-send-an-embed-via-my-discord-bot-w-python",
			)
			await message.channel.send(embed=em)


# \\\-------------------------------------------------------------------------------------///

def setup(client):
	client.add_cog(discord_py_errors(errors))