import discord, random
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select


client = commands.Bot(command_prefix = '!')

class commands(commands.Cog):

	def __init__(self, client):
		self.client = client
	


	client = commands.Bot(command_prefix = '!')

#client Commands

	#user defined commands !ping, !github, !ban user, etc
	@client.command(aliases=['8 ball', '8ball', '8 Ball'])
	async def _8ball(self, ctx, *, question):
		responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.",
		 	"Cannot predict now.", "Concentrate and ask again.",
	             	"Don’t count on it.", "It is certain.", "It is decidedly so.",
	             	 "Most likely.", "My reply is no.", "My sources say no.",
	            	 "Outlook not so good.", "Outlook good.", "Reply hazy, try again.",
	            	  "Signs point to yes.", "Very doubtful.", "Without a doubt.",
	            	 "Yes.", "Yes – definitely.", "You may rely on it."]

		await ctx.send(f'Question: [question]\nAnswer: {random.choice(responses)}')


	@client.command(aliases=['Git', 'Github', 'github', 'github link'])
	async def git(self, ctx):
		await ctx.send(f'The Github link is: https://github.com/DustinFoes')
	
	@client.command()
	async def gitrepos(self, ctx):
		repos = ['https://github.com/DustinFoes/DJANGOWEBSITE', 
		'https://github.com/DustinFoes/PyGameSpaceShooter',
		'https://github.com/DustinFoes/password-creator',
		'https://github.com/DustinFoes/Calculator-App',
		'https://github.com/DustinFoes/DiscordBotDave']
		await ctx.send(f'Github Repositories: {repos}')





	@client.command()
	async def random(self, ctx):
		n = random.randint(1, 9999)
		ctx.send(f'{n}')

	@client.command()
	async def thumbpoll(self,ctx,*,message):
		emb=discord.Embed(title='POLL ', description=f'{message}')
		msg=await ctx.channel.send(embed=emb)
		await msg.add_reaction('👍')
		await msg.add_reaction('👎')


	@client.command()
	async def facepoll(self,ctx,*,message):
		emb=discord.Embed(title='------\nPOLL\n------', description=f'{message}')
		msg=await ctx.channel.send(embed=emb)
		await msg.add_reaction('😍')
		await msg.add_reaction('😐')
		await msg.add_reaction('😡')
		await msg.add_reaction('😥')




def setup(client):
        client.add_cog(commands(client))
