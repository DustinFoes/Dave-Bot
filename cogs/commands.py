import discord, random
from discord.ext import commands
from discord_slash import SlashCommand

class commands(commands.Cog):

	def __init__(self, client):
		self.client = client
	


	client = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
	slash = SlashCommand(client, sync_commands=True)

#client Commands

	#user defined commands !ping, !github, !ban user, etc
	@slash.slash(description='Magic 8 Ball Many Mystery')
	async def _8ball(self, ctx, *, question):
		responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.",
					"Cannot predict now.", "Concentrate and ask again.",
					"Don’t count on it.", "It is certain.", "It is decidedly so.",
					 "Most likely.", "My reply is no.", "My sources say no.",
					 "Outlook not so good.", "Outlook good.", "Reply hazy, try again.",
					  "Signs point to yes.", "Very doubtful.", "Without a doubt.",
					 "Yes.", "Yes – definitely.", "You may rely on it."]

		await ctx.reply(f'Question: [question]\nAnswer: {random.choice(responses)}')

	@slash.slash(description='Gives the GitHub Link')
	async def git(self, ctx):
		await ctx.message.delete()
		await ctx.reply(f'The Github link is: https://github.com/DustinFoes')
	
	@slash.slash(description='Gives the GitHub Repos')
	async def gitrepos(self, ctx):
		await ctx.message.delete()
		repos = ['https://github.com/DustinFoes/DJANGOWEBSITE', 
		'https://github.com/DustinFoes/PyGameSpaceShooter',
		'https://github.com/DustinFoes/password-creator',
		'https://github.com/DustinFoes/Calculator-App',
		'https://github.com/DustinFoes/DiscordBotDave']
		await ctx.reply(f'Github Repositories: {repos}')





	@slash.slash(description='Sends a random number')
	async def random(self, ctx):
		n = random.randint(1, 9999)
		ctx.reply(f'{n}')

	@slash.slash(description='Creates a Poll With 👍 & 👎')
	async def thumbpoll(self,ctx,*,message):
		await ctx.message.delete()
		emb=discord.Embed(title='~~~~~~~~~~~~~\nPOLLTIME!\n~~~~~~~~~~~~~', description=f'{message}')
		msg=await ctx.channel.send(embed=emb)
		await msg.add_reaction('👍')
		await msg.add_reaction('👎')


	@slash.slash(description='Creates a Poll with 😍😐😡😥')
	async def facepoll(self,ctx,*,message):
		await ctx.message.delete()
		emb=discord.Embed(title='~~~~~~~~~~~~~\nPOLLTIME!\n~~~~~~~~~~~~~', description=f'{message}')
		msg=await ctx.channel.send(embed=emb)
		await msg.add_reaction('😍')
		await msg.add_reaction('😐')
		await msg.add_reaction('😡')
		await msg.add_reaction('😥')




def setup(client):
	client.add_cog(commands(client))