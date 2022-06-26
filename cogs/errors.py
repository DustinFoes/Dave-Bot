import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand


'''Simple Bot That Listens for common error names like syntax error, then displays information about the error type. This can be useful when
	someone is posting lines of code in request for help.'''


class errors(commands.Cog):

	def __init__(self, client):
		self.client = client
	


	client = commands.Bot(command_prefix = '')
	slash = SlashCommand(client, sync_commands=True)





# /// CLIENT COMMANDS \\\



	@slash.slash(description='Lists the different types of Python errors')
	async def Error_Types(self, ctx):
		emb=discord.Embed(title='Error Types', url='https://www.tutorialsteacher.com/python/error-types-in-python')

		emb.add_field(title='IndexError', 
			description='The IndexError is thrown when trying to access an item at an invalid index.', 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=operation%20is%20zero.-,IndexError,-The%20IndexError%20is')

		emb.add_field(title='ModuleNotFoundError', 
			description='The ModuleNotFoundError is thrown when a module could not be found.', 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=out%20of%20range-,ModuleNotFoundError,-The%20ModuleNotFoundError%20is')

		emb.add_field(title='KeyError', 
			description='The KeyError is thrown when a key is not found.', 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=named%20%27notamodule%27-,KeyError,-The%20KeyError%20is')

		emb.add_field(title='ImportError', 
			description='The ImportError is thrown when a specified function can not be found.', 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=%3A%20%274%27-,ImportError,-The%20ImportError%20is')

		emb.add_field(title='StopIteration', 
			description='The StopIteration is thrown when the next() function goes beyond the iterator items.', 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=name%20%27cube%27-,StopIteration,-The%20StopIteration%20is')

		emb.add_field(title='TypeError', 
			description='The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.', 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=it)%0AStopIteration-,TypeError,-The%20TypeError%20is')

		emb.add_field(title='ValueError', 
			description="The ValueError is thrown when a function's argument is of an inappropriate type.", 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=%2C%20not%20int-,ValueError,-The%20ValueError%20is')

		emb.add_field(title='NameError', 
			description='The NameError is thrown when an object could not be found.', 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=%3A%20%27xyz%27-,NameError,-The%20NameError%20is')

		emb.add_field(title='ZeroDivisionError', 
			description='The ZeroDivisionError is thrown when the second operator in the division is zero.', 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=is%20not%20defined-,ZeroDivisionError,-The%20ZeroDivisionError%20is')

		emb.add_field(title='KeyboardInterrupt', 
			description='KeyboardInterrupt', 
			url='https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=division%20by%20zero-,KeyboardInterrupt,-The%20KeyboardInterrupt%20is')


		msg=await ctx.channel.send(embed=emb)


# /// PYTHON ERRORS \\\

	@commands.Cog.listener()
	async def on_message(self, message):
		if "AssertionError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="AssertionError!",
				value="	Raised when the assert statement fails.",
			)
			await message.channel.send(embed=em)

		elif "AttributeError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0xdb1f1f
			)
			em.add_field(
				name="AttributeError!",
				value="Raised on the attribute assignment or reference fails.",
			)
			await message.channel.send(embed=em)

		elif "EOFError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="EOFError!",
				value="Raised when the input() function hits the end-of-file condition.",
			)
			await message.channel.send(embed=em)

		elif "FloatingPointError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="FloatingPointError!",
				value="Raised when a floating point operation fails.",
			)
			await message.channel.send(embed=em)

		elif "GeneratorExit:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="GeneratorExit	!",
				value="Raised when a generator's close() method is called.",
			)
			await message.channel.send(embed=em)

		elif "ImportError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="ImportError!",
				value="Raised when the imported module is not found.",
			)
			await message.channel.send(embed=em)

		elif "IndexError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="IndexError!",
				value="Raised when the index of a sequence is out of range.",
			)
			await message.channel.send(embed=em)

		elif "KeyError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="KeyError!",
				value="Raised when a key is not found in a dictionary.",
			)
			await message.channel.send(embed=em)

		elif "KeyboardInterrupt:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="KeyboardInterrupt!",
				value="Raised when the user hits the interrupt key (Ctrl+c or delete).",
			)
			await message.channel.send(embed=em)

		elif "MemoryError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="MemoryError!",
				value="Raised when an operation runs out of memory.",
			)
			await message.channel.send(embed=em)

		elif "NameError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="NameError!",
				value="Raised when a variable is not found in the local or global scope.",
			)
			await message.channel.send(embed=em)

		elif "NotImplementedError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="NotImplementedError!",
				value="Raised by abstract methods.",
			)
			await message.channel.send(embed=em)

		elif "OSError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="OSError!",
				value="Raised when a system operation causes a system-related error.",
			)
			await message.channel.send(embed=em)

		elif "OverflowError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="OverflowError!",
				value="Raised when the result of an arithmetic operation is too large to be represented.",
			)
			await message.channel.send(embed=em)

		elif "ReferenceError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="ReferenceError!",
				value="Raised when a weak reference proxy is used to access a garbage collected referent.",
			)
			await message.channel.send(embed=em)

		elif "RuntimeError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="RuntimeError!",
				value="Raised when an error does not fall under any other category.",
			)
			await message.channel.send(embed=em)

		elif "StopIteration:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="StopIteration	!",
				value="Raised by the next() function to indicate that there is no further item to be returned by the iterator.",
			)
			await message.channel.send(embed=em)

		elif "SyntaxError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="SyntaxError!",
				value="Raised by the parser when a syntax error is encountered.",
			)
			await message.channel.send(embed=em)

		elif "IndentationError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="IndentationError!",
				value="Raised when there is an incorrect indentation.",
			)
			await message.channel.send(embed=em)

		elif "TabError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="TabError!",
				value="Raised when the indentation consists of inconsistent tabs and spaces.",
			)
			await message.channel.send(embed=em)

		elif "SystemError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="SystemError!",
				value="Raised when the interpreter detects internal error.",
			)
			await message.channel.send(embed=em)

		elif "SystemExit:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="SystemExit!",
				value="Raised by the sys.exit() function.",
			)
			await message.channel.send(embed=em)

		elif "TypeError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="TypeError!",
				value="Raised when a function or operation is applied to an object of an incorrect type.",
			)
			await message.channel.send(embed=em)

		elif "UnboundLocalError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnboundLocalError!",
				value="Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.",
			)
			await message.channel.send(embed=em)

		elif "UnicodeError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnicodeError!",
				value="Raised when there is an incorrect indentation.",
			)
			await message.channel.send(embed=em)

		elif "UnicodeEncodeError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnicodeEncodeError!",
				value="Raised when the indentation consists of inconsistent tabs and spaces.",
			)
			await message.channel.send(embed=em)

		elif "UnicodeDecodeError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnicodeDecodeError!",
				value="Raised when the interpreter detects internal error.",
			)
			await message.channel.send(embed=em)

		elif "UnicodeTranslateError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnicodeTranslateError!",
				value="Raised by the sys.exit() function.",
			)
			await message.channel.send(embed=em)

		elif "ValueError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="ValueError!",
				value="Raised when a function or operation is applied to an object of an incorrect type.",
			)
			await message.channel.send(embed=em)

		elif "ZeroDivisionError:" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="ZeroDivisionError!",
				value="Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.",
			)
			await message.channel.send(embed=em)

def setup(client):
	client.add_cog(errors(errors))