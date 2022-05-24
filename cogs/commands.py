import discord, random
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

class commands(commands.Cog):

	def __init__(self, client):
		self.client = client
		
	repos = ['https://github.com/DustinFoes/DJANGOWEBSITE', 
		'https://github.com/DustinFoes/PyGameSpaceShooter',
		'https://github.com/DustinFoes/password-creator',
		'https://github.com/DustinFoes/Calculator-App',
		'https://github.com/DustinFoes/DiscordBotDave']


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

	@client.command(aliases=['Gitrepos', 'Github repos', 'github repos','repos', 'reposetories'])
	async def gitrepos(self, ctx):
		await ctx.send(f'Github Repositories: , {repos}')


	@client.command()
	async def kick(self, ctx, member : discord.Member, *, reason=None):
		await member.kick(reason=reason)

	@client.command()
	async def random(self, ctx):
		n = random.randint(1, 9999)
		ctx.send(f'{n}')

	#These are pretty self explanatory

	@client.command()
	async def ban(self, ctx, member : discord.Member, *, reason=None):
		await member.ban(reason=reason)

	@client.command()
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user

			if(user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'Unnbanned: {user.name}#{user.discriminator}')
				return
	

def setup(client):
        client.add_cog(commands(client))
