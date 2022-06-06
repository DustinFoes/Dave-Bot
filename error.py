import discord, random, os #imports the discord.py 
from discord.ext import commands, tasks #allows us to create commands in discord
from itertools import cycle
from discord.utils import get
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

@client.event
async def on_ready(): #when the bot is in ready mode/state, then do this:
	print('DAVE is Online')
	change_status.start()
	send_message.start()



@client.event
async def on_guild_join(join):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = '!'

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f)


@client.command(aliases=['purge', 'clean', 'delete'])
@commands.check(server_owner)
async def clear(ctx, amount : int):
	await client.delete_messages(limit=int) 
''' !clear X will clear a specified number of messages from the channel'''


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)



@tasks.loop(seconds=3)
async def change_status():
        await client.change_presence(activity=discord.Game(next(status)))


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

	
@client.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")


@tasks.loop(minutes=5.0)
async def send_message():
	channel = client.get_channel(978762893954805830)
	await channel.send("Use !new to create a new ticket!\nUse !close to close the ticket")



@client.command()
async def new(ctx, *, args = None):
    await ctx.message.delete()
    await client.wait_until_ready()

    if args == None:
        message_content = "Please give a brief description of your issue and we will be with you shortly:"
    
    else:
        message_content = "".join(args)

    with open("data.json") as f:
        data = json.load(f)

    ticket_number = int(data["ticket-counter"])
    ticket_number += 1
    ticket_channel = await ctx.guild.create_text_channel("ticket-{}".format(ticket_number))
    await ctx.guild.create_category('TICKETS', overwrites=None, reason=None)

    await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)

    for role_id in data["valid-roles"]:
        role = ctx.guild.get_role(role_id)

        await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
    
    await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    em = discord.Embed(title="New ticket from {}#{}".format(ctx.author.name, ctx.author.discriminator), description= "Ticket Message: {} \n\nPlease provide details for your issue and wait for assistance".format(message_content), color=0x00a8ff)

    await ticket_channel.send(embed=em)

    pinged_msg_content = ""
    non_mentionable_roles = []

    if data["pinged-roles"] != []:

        for role_id in data["pinged-roles"]:
            role = ctx.guild.get_role(role_id)

            pinged_msg_content += role.mention
            pinged_msg_content += " "

            if role.mentionable:
                pass
            else:
                await role.edit(mentionable=True)
                non_mentionable_roles.append(role)
        
        await ticket_channel.send(pinged_msg_content)

        for role in non_mentionable_roles:
            await role.edit(mentionable=False)
    
    data["ticket-channel-ids"].append(ticket_channel.id)

    data["ticket-counter"] = int(ticket_number)
    with open("data.json", 'w') as f:
        json.dump(data, f)
    
    created_em = discord.Embed(title="Help Tickets", description="Your ticket has been created at {} \n\n Please provide details for your issue and wait for assistance".format(ticket_channel.mention), color=0x00a8ff)
    
    await ctx.send(embed=created_em)



for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run('OTc0NzEwNTc3ODMyMjg0MTcw.GTKKWM.v5SiXjCVzQOwr3Z5A2oSyJ138OTwEy7DIxdh1g')
