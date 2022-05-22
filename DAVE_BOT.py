import discord, random, os #imports the discord.py 
from discord.ext import commands #allows us to create commands in discord


client = commands.Bot(command_prefix = '!')

#client events
# client events: when the bot sees this happen, it will do this
@client.event
async def on_ready(): #when the bot is in ready mode/state, then do this:
	await client,change_presence(status=discord.Status.idle, activity=discord.Game('Helping Hand'))
	print('DAVE is Online')

@client.event
async def on_member_join(member):
	print(f'{member} has joined the server!')


@client.event
async def on_member_remove(member):
	print(f'{member} has left the server...')

#client commands

@client.command()
async def load(ctx, extension): #extention = the cog you want to load
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'Cog has been loaded')

@client.command()
async def unload(ctx, extension): #extention = the cog you want to load
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f'Cog has been unloaded')	

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'Cog has been reloaded')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! I took {round(client.latency * 1000)}ms to respond.')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run('OTc0NzEwNTc3ODMyMjg0MTcw.GTKKWM.v5SiXjCVzQOwr3Z5A2oSyJ138OTwEy7DIxdh1g')