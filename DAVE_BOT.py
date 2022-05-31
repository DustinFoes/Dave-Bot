import discord, random, os #imports the discord.py 
from discord.ext import commands, tasks #allows us to create commands in discord
from itertools import cycle
import json
import traceback
import datetime


'''def get_prefix(client, message):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	return prefixes[str(message.guild.id)]'''



class CustomHelpCommand(commands.HelpCommand):

	def __init__(self):
		super().__init__()

	async def send_bot_help(self, mapping):
		for cog in mapping:
			await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in mapping[cog]]}')


	async def send_cog_help(self, cog):
		await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')

	async def send_group_help(self, group):
		await self.get_destination().send(f'{group.name}: {[command.name for index, command in enumerate(group.commands)]}')


	async def send_command_help(self, command):
		await self.get_destination().send(command.name)








prefix = '!'
client = commands.Bot(command_prefix = prefix, HelpCommand=CustomHelpCommand())

status = cycle(['Valorant', 'Your Mom'])


def server_owner(ctx):
	return ctx.author.id == 221840898634285056 # <--- This sets a master user to have access to specific functions.


#client events
# client events: when the bot sees this happen, it will do this
@client.event
async def on_ready(): #when the bot is in ready mode/state, then do this:
	print('DAVE is Online')
	change_status.start()



@client.event
async def on_guild_join(join):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = '!'

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f)



'''@client.event
async def on_message_react
@client.event
  async def on_command_error(self, ctx, error):
       # if command has local error handler, return
       if hasattr(ctx.command, 'on_error'):
            return

        # get the original exception
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            return

        if isinstance(error, commands.BotMissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)
            await ctx.send(_message)
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send('This command has been disabled.')
            return

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
            return

        if isinstance(error, commands.MissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = 'You need the **{}** permission(s) to use this command.'.format(fmt)
            await ctx.send(_message)
            return

        if isinstance(error, commands.UserInputError):
            await ctx.send("Invalid input.")
            await self.send_command_help(ctx)
            return

        if isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send('This command cannot be used in direct messages.')
            except discord.Forbidden:
                pass
            return

        if isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have permission to use this command.")
            return

        # ignore all other exception types, but print them to stderr
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)

        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)'''

@client.event
async def on_guild_remove(guild):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes.pop(str(guild.id))

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f)

@client.event
async def on_member_join(member):
	print(f'{member} has joined the server!')


@client.event
async def on_member_remove(member):
	print(f'{member} has left the server...')

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("I'm sorry, I Don't Recognize That Command. For Help, type !help")


#client commands

@client.command(aliases=['purge', 'clean', 'delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)
''' !clear X will clear a specified number of messages from the channel'''

@clear.error
async def clear_error(ctx, error):
	await ctx.send("That Didn't Work")


@client.command(aliases=['purge_all', 'clean_all', 'delete_all'])
@commands.has_permissions(manage_messages=True)
async def clearall(ctx, amount=999):
	await ctx.channel.purge(limit=amount)
	
'''clears up to 999 msgs,
if you want more type a higher number after the command
ex: !clear all 999999
NOTE: this function cannot have aliases due to the fact that the command is looking for a input 
after clearall to specify the amount to clear'''

@clearall.error
async def clearall_error(ctx, error):
	await ctx.send('That Didnt Work')

@client.command()
@commands.check(server_owner)
async def load(ctx, extension): #extension = the cog you want to load
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'Cog has been loaded')

@client.command()
@commands.check(server_owner)
async def unload(ctx, extension): #extension = the cog you want to load
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f'Cog has been unloaded')	

@client.command()
@commands.check(server_owner)
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'Cog has been reloaded')

@reload.error
async def check_error(ctx, error):
	await ctx.send('Reload Failed')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! I took {round(client.latency * 1000)}ms to respond.')

@tasks.loop(seconds=3)
async def change_status():
        await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def slowmode(ctx, amount: 5):
    await ctx.channel.edit(slowmode_delay=amount)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

@slowmode.error
async def slowmode_error(ctx, error):
	await ctx.send('An Unknown Error Occurred')




        
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@kick.error
async def kick_error(ctx, error):
	await ctx.send('An Error Occurred')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)





@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if(user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unnbanned: {user.name}#{user.discriminator}')
			return
	





for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run('OTc0NzEwNTc3ODMyMjg0MTcw.GTKKWM.v5SiXjCVzQOwr3Z5A2oSyJ138OTwEy7DIxdh1g')
