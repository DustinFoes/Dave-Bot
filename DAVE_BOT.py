from unicodedata import category
import discord, random, os #imports the discord.py 
from discord.ext import commands, tasks #allows us to create commands in discord
from itertools import cycle
import json
import traceback
import logging
import datetime
from discord.ext.commands import has_permissions, MissingPermissions
from discord_slash import SlashCommand
import asyncio


print("//////////////////////////////////////////////////////////")
print("//                                                      //")
print("//        * *      * *    *     *  * * * *              //")
print("//        *   *  *     *  *     *  *                    //")
print("//        *   *  * *** *   *   *   * * *                //")
print("//        *   *  *     *    * *    *                    //")
print("//        * *    *     *     *     * * * * *            //")
print("//                                                      //")
print("//////////////////////////////////////////////////////////")


if os.path.exists(os.getcwd() + '/config.json'):
	with open('./config.json') as f:
		configData = json.load(f)
else:
	configTemplate = {'TOKEN': '', 'OWNER_ID': ''}

	with open(os.getcwd() + '/config.json', 'w+') as f:
		json.dump(configTemplate, f)


TOKEN = configData['TOKEN']
OWNER_ID = configData['OWNER_ID']
TICKET_CHANNEL = configData['TICKET_CHANNEL']
CATEGORY = configData['CATEGORY']

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


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




client = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
slash = SlashCommand(client, sync_commands=True)
status = cycle(['Valorant', 'Your Mom'])



client.remove_command("help")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

def server_owner(ctx):
    return ctx.author.id == OWNER_ID # <--- This sets a master user to have access to specific functions.


#client events
# client events: when the bot sees this happen, it will do this
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
        await ctx.send("I'm sorry, I Don't Recognize That Command. For Help, type /help")


#client commands

@slash.slash(description='clears x amount of messages from chat')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    Embed = discord.Embed(title = '✅ Success!', 
        description=f'{ctx.author.mention} cleared {amount} messages!', color = 0x00ff00)
    await ctx.reply(embed=Embed)
''' !clear X will clear a specified number of messages from the channel'''

@clear.error
async def clear_error(ctx, error):
    Embed = discord.Embed(title = '❌ Failed!', 
        description=f'Failed To Clear Messages', color = 0x00ff00)
    await ctx.reply(embed=Embed)


@slash.slash(description='clears / Nukes Chat')
@commands.has_permissions(manage_messages=True)
async def clearall(ctx, amount=999):
    await ctx.channel.purge(limit=amount)
    Embed = discord.Embed(title = '✅ Success!', description=f'{ctx.author.mention} 💣Nuked the Channel', color = 0x00ff00)
    await ctx.reply(embed=Embed)
    
'''clears up to 999 msgs,
if you want more type a higher number after the command
ex: !clear all 999999
NOTE: this function cannot have aliases due to the fact that the command is looking for a input 
after clearall to specify the amount to clear'''



@slash.slash(description='Loads a specifiec cog')
@commands.check(server_owner)
async def load(ctx, extension): #extension = the cog you want to load
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog has been loaded')

@slash.slash(description='Unloads a specifiec cog')
@commands.check(server_owner)
async def unload(ctx, extension): #extension = the cog you want to load
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog has been unloaded')    

@slash.slash(description='Reloads a specific cog')
@commands.check(server_owner)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog has been reloaded')

@reload.error
async def check_error(ctx, error):
    await ctx.message.delete()
    await ctx.send('Reload Failed')

@slash.slash(description='Returns the bots ping')
async def ping(ctx):
    await ctx.send(f'Pong! I took {round(client.latency * 1000)}ms to respond.')

@tasks.loop(seconds=3)
async def change_status():
        await client.change_presence(activity=discord.Game(next(status)))

@slash.slash(description='Sets slowmode')
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

@slowmode.error
async def slowmode_error(ctx, error):
    await ctx.send('An Unknown Error Occurred')


@tasks.loop(hours = 2)
async def send_message():
    channel = client.get_channel(TICKET_CHANNEL)
    await channel.send("Use !new to create a new ticket!\nUse !close to close the ticket")

        
@slash.slash(description='Kicks a user from the guild')
async def kick(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.kick(reason=reason)

@kick.error
async def kick_error(ctx, error):
    await ctx.message.delete()
    await ctx.send('An Error Occurred')

@slash.slash(description='Bans a user from the guild')
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.ban(reason=reason)





@slash.slash(description='Unbans a user from the guild')
async def unban(ctx, *, member):
    await ctx.message.delete()
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unnbanned: {user.name}#{user.discriminator}')
            return

@slash.slash(description='Shows The Davebot Weblink')
async def DaveSite(ctx):
    em = discord.Embed(title="Dave Bot Site", url="https://stonercraft.online", color=0xc44800)
    await ctx.reply(embed=em)
    
@slash.slash(description='Shows The Davebot WikiLink')
async def wiki(ctx):
    em = discord.Embed(title="Dave Bot Wiki", url="https://stonercraft.online/dave-info", color=0xc44800)
    await ctx.reply(embed=em)


@slash.slash(description='Displays the Admin Help Menu')
@has_permissions(administrator=True)
async def adminhelp(ctx):
    with open("data.json") as f:
        data = json.load(f)


        em = discord.Embed(title="Dave Bot Help", description="", color=0xc44800)
        em.add_field(name="`!clearall`", value="This command will delete the last 999 messages in the channel.")
        em.add_field(name="`!clear <value>`", value="This command will delete the specified number of messages from a channel. Default = 5")
        em.add_field(name="`!addaccess <role_id>`", value="This can be used to give a specific role access to all tickets. This command can only be run if you have an admin-level role for this bot.")
        em.add_field(name="`!delaccess <role_id>`", value="This can be used to remove a specific role's access to all tickets. This command can only be run if you have an admin-level role for this bot.")
        em.add_field(name="`!addpingedrole <role_id>`", value="This command adds a role to the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.")
        em.add_field(name="`!delpingedrole <role_id>`", value="This command removes a role from the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.")
        em.add_field(name="`!addadminrole <role_id>`", value="This command gives all users with a specific role access to the admin-level commands for the bot, such as `.addpingedrole` and `.addaccess`. This command can only be run by users who have administrator permissions for the entire server.")
        em.add_field(name="`!deladminrole <role_id>`", value="This command removes access for all users with the specified role to the admin-level commands for the bot, such as `.addpingedrole` and `.addaccess`. This command can only be run by users who have administrator permissions for the entire server.")
        em.add_field(name="`!load <cogname>`", value="This command will load the given cog.")
        em.add_field(name="`!unload <cogname>`", value="This command will unload the given cog.")
        em.add_field(name="`!reload <cogname>`", value="This command will reload the given cog.")
        em.add_field(name="`!slowmode <seconds>`", value="This command will enable slowmode for x amount of seconds.")
        em.add_field(name="`!help`", value="This command will display the normal help menu")
        em.add_field(name="`!adminhelp`", value="This command will display this menu")
        em.set_footer(text="Dave Bot")

        await ctx.reply(embed=em)


@slash.slash(description='Shows the basic help menu')
async def help(ctx):
    with open("data.json") as f:
        data = json.load(f)


        em = discord.Embed(title="Dave Bot Admin Help", description="", color=0x22fc00)
        em.add_field(name="`!new <message>`", value="This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket.")
        em.add_field(name="`!close`", value="Use this to close a ticket. This command only works in ticket channels.")
        em.add_field(name="`!8ball <question>`", value="Ask the 8 ball a question.")
        em.add_field(name="`!git`", value="This command will send a msg with the git link")
        em.add_field(name="`!gitrepos`", value="This command will display the repos in my git")
        em.add_field(name="`!random`", value="This command will give a random 4 digit number")
        em.add_field(name="`!help`", value="This command will display this menu")
        em.add_field(name="`!adminhelp`", value="This command will display th menu")
        em.set_footer(text="Dave Bot")

        await ctx.reply(embed=em)

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

    c = discord.utils.get(ctx.guild.categories, id=CATEGORY)
    ticket_number = int(data["ticket-counter"])
    ticket_number += 1
    ticket_channel = await ctx.guild.create_text_channel("ticket-{}".format(ticket_number), category=c)
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

@client.command()
async def close(ctx):
    await ctx.message.delete()
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "close"

        try:

            em = discord.Embed(title="Dave Bot's Tickets", description="Are you sure you want to close this ticket? Reply with `close` to confirm", color=0x00a8ff)
        
            await ctx.send(embed=em)
            await client.wait_for('message', check=check, timeout=60)
            await ctx.channel.delete()

            index = data["ticket-channel-ids"].index(channel_id)
            del data["ticket-channel-ids"][index]

            with open('data.json', 'w') as f:
                json.dump(data, f)
        
        except asyncio.TimeoutError:
            em = discord.Embed(title="Dave Bot's Tickets", description="You have run out of time to close this ticket. Please run the command again.", color=0x00a8ff)
            await ctx.send(embed=em)


        

@slash.slash(description='Gives a user acces to /new')
async def addaccess(ctx, role_id=None):
    await ctx.message.delete()

    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass
    
    if valid_user or ctx.author.guild_permissions.administrator:
        role_id = int(role_id)

        if role_id not in data["valid-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["valid-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)
                
                em = discord.Embed(title="Dave Bot", description="You have successfully added `{}` to the list of roles with access to tickets.".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(title="Dave Bot", description="That isn't a valid role ID. Please try again with a valid role ID.")
                await ctx.send(embed=em)
        
        else:
            em = discord.Embed(title="Dave Bot", description="That role already has access to tickets!", color=0x00a8ff)
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Dave Bot", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
        await ctx.send(embed=em)

@slash.slash(description='Removes a users access to use /new')
async def delaccess(ctx, role_id=None):
    await ctx.message.delete()
    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            valid_roles = data["valid-roles"]

            if role_id in valid_roles:
                index = valid_roles.index(role_id)

                del valid_roles[index]

                data["valid-roles"] = valid_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Dave Bot", description="You have successfully removed `{}` from the list of roles with access to tickets.".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)
            
            else:
                
                em = discord.Embed(title="Dave Bot", description="That role already doesn't have access to tickets!", color=0x00a8ff)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(title="Dave Bot", description="That isn't a valid role ID. Please try again with a valid role ID.")
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Dave Bot", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
        await ctx.send(embed=em)

@slash.slash(description='Adds a role to ping when a ticket is created')
async def addpingedrole(ctx, role_id=None):
    await ctx.message.delete()

    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass
    
    if valid_user or ctx.author.guild_permissions.administrator:

        role_id = int(role_id)

        if role_id not in data["pinged-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["pinged-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Dave Bot", description="You have successfully added `{}` to the list of roles that get pinged when new tickets are created!".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(title="Dave Bot", description="That isn't a valid role ID. Please try again with a valid role ID.")
                await ctx.send(embed=em)
            
        else:
            em = discord.Embed(title="Dave Bot", description="That role already receives pings when tickets are created.", color=0x00a8ff)
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Dave Bot", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
        await ctx.send(embed=em)

@slash.slash(description='Deletes a role from being pinged when /new is used')
async def delpingedrole(ctx, role_id=None):
    await ctx.message.delete()

    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass
    
    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            pinged_roles = data["pinged-roles"]

            if role_id in pinged_roles:
                index = pinged_roles.index(role_id)

                del pinged_roles[index]

                data["pinged-roles"] = pinged_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Dave Bot", description="You have successfully removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x00a8ff)
                await ctx.send(embed=em)
            
            else:
                em = discord.Embed(title="Dave Bot", description="That role already isn't getting pinged when new tickets are created!", color=0x00a8ff)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(title="Dave Bot", description="That isn't a valid role ID. Please try again with a valid role ID.")
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Dave Bot", description="Sorry, you don't have permission to run that command.", color=0x00a8ff)
        await ctx.send(embed=em)


@slash.slash(description='Adds a role to the adminsetting of the tickets')
@has_permissions(administrator=True)
async def addadminrole(ctx, role_id=None):
    await ctx.message.delete()

    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        data["verified-roles"].append(role_id)

        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        em = discord.Embed(title="Dave Bot", description="You have successfully added `{}` to the list of roles that can run admin-level commands!".format(role.name), color=0x00a8ff)
        await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Dave Bot", description="That isn't a valid role ID. Please try again with a valid role ID.")
        await ctx.send(embed=em)

@slash.slash(description='Deletes a role from the adminsettting of the tickets')
@has_permissions(administrator=True)
async def deladminrole(ctx, role_id=None):
    await ctx.message.delete()
    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        admin_roles = data["verified-roles"]

        if role_id in admin_roles:
            index = admin_roles.index(role_id)

            del admin_roles[index]

            data["verified-roles"] = admin_roles

            with open('data.json', 'w') as f:
                json.dump(data, f)
            
            em = discord.Embed(title="Dave Bot", description="You have successfully removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x00a8ff)

            await ctx.send(embed=em)
        
        else:
            em = discord.Embed(title="Dave Bot", description="That role isn't getting pinged when new tickets are created!", color=0x00a8ff)
            await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Dave Bot", description="That isn't a valid role ID. Please try again with a valid role ID.")
        await ctx.send(embed=em)

@slash.slash(description='Displays the DaveBot Invite Link')
async def invite(ctx, role_id=None):
    em = discord.Embed(title="Dave Bot Invite Link", url="https://discord.com/api/oauth2/authorize?client_id=974710577832284170&permissions=8&scope=bot%20applications.commands", color=0xc44800)
    await ctx.reply(embed=em)

@slash.slash(description='Magic 8 Ball Many Mystery')
async def _8ball(ctx, *, question):
	responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.",
	 			"Cannot predict now.", "Concentrate and ask again.",
             	"Don’t count on it.", "It is certain.", "It is decidedly so.",
             	 "Most likely.", "My reply is no.", "My sources say no.",
            	 "Outlook not so good.", "Outlook good.", "Reply hazy, try again.",
            	  "Signs point to yes.", "Very doubtful.", "Without a doubt.",
            	 "Yes.", "Yes – definitely.", "You may rely on it."]

	await ctx.reply(f'Question: [question]\nAnswer: {random.choice(responses)}')

@slash.slash(description='Gives the GitHub Link')
async def git(ctx):
	await ctx.message.delete()
	await ctx.reply(f'The Github link is: https://github.com/DustinFoes')

@slash.slash(description='Gives the GitHub Repos')
async def gitrepos(ctx):
	repos = ['https://github.com/DustinFoes/DJANGOWEBSITE', 
	'https://github.com/DustinFoes/PyGameSpaceShooter',
	'https://github.com/DustinFoes/password-creator',
	'https://github.com/DustinFoes/Calculator-App',
	'https://github.com/DustinFoes/DiscordBotDave']
	await ctx.reply(f'Github Repositories: {repos}')





@slash.slash(description='Sends a random number')
async def random(ctx):
	n = random.randint(1, 9999)
	ctx.reply(f'{n}')

@slash.slash(description='Creates a Poll With 👍 & 👎')
async def thumbpoll(ctx,*,message):
	await ctx.message.delete()
	emb=discord.Embed(title='~~~~~~~~~~~~ ~\nPOLLTIME!\n~~~~~~~~~~~~~', description=f'{message}')
	msg=await ctx.channel.reply(embed=emb)
	await msg.add_reaction('👍')
	await msg.add_reaction('👎')


@slash.slash(description='Creates a Poll with 😍😐😡😥')
async def facepoll(ctx,*,message):
	await ctx.message.delete()
	emb=discord.Embed(title='~~~~~~~~~~~~~\nPOLLTIME!\n~~~~~~~~~~~~~', description=f'{message}')
	msg=await ctx.channel.reply(embed=emb)
	await msg.add_reaction('😍')
	await msg.add_reaction('😐')
	await msg.add_reaction('😡')
	await msg.add_reaction('😥')



client.run(TOKEN)