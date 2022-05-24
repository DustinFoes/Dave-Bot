import discord, random, os #imports the discord.py 
from discord.ext import commands, tasks #allows us to create commands in discord
from itertools import cycle

client = commands.Bot(command_prefix = '!')
status = cycle(['Valorant', 'Your Mom'])


#client events
# client events: when the bot sees this happen, it will do this
@client.event
async def on_ready(): #when the bot is in ready mode/state, then do this:
	print('DAVE is Online')
	change_status.start()

@client.event
async def on_member_join(member):
	print(f'{member} has joined the server!')


@client.event
async def on_member_remove(member):
	print(f'{member} has left the server...')

@client.event
async def on_command_error(ctx, error):
	pass


#client commands

@client.command()
async def clear(ctx, amount : int):
	await ctx.channel.purge(limit=amount)   
''' !clear 50 will clears a specified number of messages from the channel'''

@clear.error
async def clear_error(ctx, error):
	await ctx.send('Please specify the # of messages to delete')

@client.command()
async def clearall(ctx, amount=999):
	await ctx.channel.purge(limit=amount)     
'''clears up to 999 msgs,
if you want more type a higher number after the command
ex: !clear all 999999
NOTE: this function cannot have alieses due to the fact that the command is looking for a input 
after clearall to specify the ammount to clear'''

@client.command()
async def load(ctx, extension): #extension = the cog you want to load
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'Cog has been loaded')

@client.command()
async def unload(ctx, extension): #extension = the cog you want to load
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

@tasks.loop(seconds=3)
async def change_status():
        await client.change_presence(activity=discord.Game(next(status)))
        

	

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run('OTc0NzEwNTc3ODMyMjg0MTcw.GTKKWM.v5SiXjCVzQOwr3Z5A2oSyJ138OTwEy7DIxdh1g')
