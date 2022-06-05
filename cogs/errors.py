import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio


client = commands.Bot(command_prefix = '!')

class commands(errormsgBot.Cog):

	def __init__(self, client):
		self.client = client
	


	client = commands.Bot(command_prefix = '!')


# @client.Events
	
	@client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('AssertionError'):
        await message.channel.send('Ive detected a common error in your code.\nAssertionError!: Raised when the assert statement fails.')

        em = discord.Embed(title = "Coding Error Detected", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)


	@client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('AttributeError'):
        await message.channel.send('Ive detected a common error in your code.\nAttributeError!: Raised when the assert statement fails.')

        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('EOFError'):
        await message.channel.send('Ive detected a common error in your code.\nEOFError!: Raised on the attribute assignment or reference fails.')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('FloatingPointError'):
        await message.channel.send('Ive detected a common error in your code.\nFloatingPointError!: Raised when the input() function hits the end-of-file condition.')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('GeneratorExit'):
        await message.channel.send('Ive detected a common error in your code.\nGeneratorExit!: Raised when a floating point operation fails.')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('ImportError'):
        await message.channel.send("Ive detected a common error in your code.\nImportError!: Raised when a generator's close() method is called.")
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('IndexError'):
        await message.channel.send('Ive detected a common error in your code.\nIndexError!: Raised when the imported module is not found.')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('KeyError'):
        await message.channel.send('Ive detected a common error in your code.\nKeyError!: Raised when the index of a sequence is out of range.')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('KeyboardInterrupt'):
        await message.channel.send('Ive detected a common error in your code.\nKeyboardInterrupt!: Raised when a key is not found in a dictionary.')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('MemoryError'):
        await message.channel.send('Ive detected a common error in your code.\nMemoryError!: Raised when the user hits the interrupt key (Ctrl+c or delete).')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('NameError'):
        await message.channel.send('Ive detected a common error in your code.\nNameError!: Raised when an operation runs out of memory.')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('NotImplementedError'):
        await message.channel.send('Ive detected a common error in your code.\nNotImplementedError!: 	Raised when a variable is not found in the local or global scope.')
    	
    	em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('OSError'):
        await message.channel.send('Ive detected a common error in your code.\nNotImplementedError!: OSError')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('OverflowError'):
        await message.channel.send('Ive detected a common error in your code.\nOverflowError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('ReferenceError'):
        await message.channel.send('Ive detected a common error in your code.\nReferenceError: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('RuntimeError'):
        await message.channel.send('Ive detected a common error in your code.\nRuntimeError!: ')
            
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)    


    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('StopIteration'):
        await message.channel.send('Ive detected a common error in your code.\nStopIteration!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('SyntaxError'):
        await message.channel.send('Ive detected a common error in your code.\n!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('IndentationError'):
        await message.channel.send('Ive detected a common error in your code.\nSyntaxError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('TabError'):
        await message.channel.send('Ive detected a common error in your code.\nIndentationError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)  


  	@client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('SystemError'):
        await message.channel.send('Ive detected a common error in your code.\nATabError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('SystemExit'):
        await message.channel.send('Ive detected a common error in your code.\nSystemError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('TypeError'):
        await message.channel.send('Ive detected a common error in your code.\nSystemExit!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)    


    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('UnboundLocalError'):
        await message.channel.send('Ive detected a common error in your code.\nTypeError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('UnicodeError'):
        await message.channel.send('Ive detected a common error in your code.\nUnboundLocalError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('UnicodeEncodeError'):
        await message.channel.send('Ive detected a common error in your code.\nUnicodeError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('UnicodeDecodeError'):
        await message.channel.send('Ive detected a common error in your code.\nUnicodeEncodeError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)  


    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('UnicodeTranslateError'):
        await message.channel.send('Ive detected a common error in your code.\nUnicodeDecodeError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('ValueError'):
        await message.channel.send('Ive detected a common error in your code.\nVUnicodeTranslateError!: ')
        
        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)

    @client.event()
	async def on_message(self, *, ctx, message):
    if message.author == client.user:
        return

    if message.content.('ZeroDivisionError'):
        await message.channel.send('Ive detected a common error in your code.')

        em = discord.Embed(title = "Coding Error Detection", description ="", color = 0x22fc00)
        em.add_field(name="ValueError!:")
        await ctx.send(embed=em)