import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio



class errors(commands.Cog):

	def __init__(self, client):
		self.client = client
	


	client = commands.Bot(command_prefix = '!')

	@commands.Cog.listener()
	async def on_message(self, message):
		if "AssertionError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="AssertionError!",
				value="	Raised when the assert statement fails.",
			)
			await message.channel.send(embed=em)

		elif "AttributeError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="AttributeError!",
				value="Raised on the attribute assignment or reference fails.",
			)
			await message.channel.send(embed=em)

		elif "EOFError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="EOFError!",
				value="Raised when the input() function hits the end-of-file condition.",
			)
			await message.channel.send(embed=em)

		elif "FloatingPointError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="FloatingPointError!",
				value="Raised when a floating point operation fails.",
			)
			await message.channel.send(embed=em)

		elif "GeneratorExit	" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="GeneratorExit	!",
				value="Raised when a generator's close() method is called.",
			)
			await message.channel.send(embed=em)

		elif "ImportError	" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="ImportError!",
				value="Raised when the imported module is not found.",
			)
			await message.channel.send(embed=em)

		elif "IndexError	" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="IndexError	!",
				value="Raised when the index of a sequence is out of range.",
			)
			await message.channel.send(embed=em)

		elif "KeyError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="KeyError!",
				value="Raised when a key is not found in a dictionary.",
			)
			await message.channel.send(embed=em)

		elif "KeyboardInterrupt" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="KeyboardInterrupt!",
				value="Raised when the user hits the interrupt key (Ctrl+c or delete).",
			)
			await message.channel.send(embed=em)

		elif "MemoryError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="MemoryError!",
				value="Raised when an operation runs out of memory.",
			)
			await message.channel.send(embed=em)

		elif "NameError	" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="NameError	!",
				value="Raised when a variable is not found in the local or global scope.",
			)
			await message.channel.send(embed=em)

		elif "NotImplementedError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="NotImplementedError!",
				value="Raised by abstract methods.",
			)
			await message.channel.send(embed=em)

		elif "OSError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="OSError!",
				value="Raised when a system operation causes a system-related error.",
			)
			await message.channel.send(embed=em)

		elif "OverflowError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="OverflowError!",
				value="Raised when the result of an arithmetic operation is too large to be represented.",
			)
			await message.channel.send(embed=em)

		elif "ReferenceError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="ReferenceError!",
				value="Raised when a weak reference proxy is used to access a garbage collected referent.",
			)
			await message.channel.send(embed=em)

		elif "RuntimeError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="RuntimeError!",
				value="Raised when an error does not fall under any other category.",
			)
			await message.channel.send(embed=em)

		elif "StopIteration	" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="StopIteration	!",
				value="Raised by the next() function to indicate that there is no further item to be returned by the iterator.",
			)
			await message.channel.send(embed=em)

		elif "SyntaxError	" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="SyntaxError!",
				value="Raised by the parser when a syntax error is encountered.",
			)
			await message.channel.send(embed=em)

		elif "IndentationError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="IndentationError!",
				value="Raised when there is an incorrect indentation.",
			)
			await message.channel.send(embed=em)

		elif "TabError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="TabError!",
				value="Raised when the indentation consists of inconsistent tabs and spaces.",
			)
			await message.channel.send(embed=em)

		elif "SystemError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="SystemError!",
				value="Raised when the interpreter detects internal error.",
			)
			await message.channel.send(embed=em)

		elif "SystemExit" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="SystemExit!",
				value="Raised by the sys.exit() function.",
			)
			await message.channel.send(embed=em)

		elif "TypeError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="TypeError!",
				value="Raised when a function or operation is applied to an object of an incorrect type.",
			)
			await message.channel.send(embed=em)

		elif "UnboundLocalError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnboundLocalError!",
				value="Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.",
			)
			await message.channel.send(embed=em)

		elif "UnicodeError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnicodeError!",
				value="Raised when there is an incorrect indentation.",
			)
			await message.channel.send(embed=em)

		elif "UnicodeEncodeError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnicodeEncodeError!",
				value="Raised when the indentation consists of inconsistent tabs and spaces.",
			)
			await message.channel.send(embed=em)

		elif "UnicodeDecodeError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnicodeDecodeError!",
				value="Raised when the interpreter detects internal error.",
			)
			await message.channel.send(embed=em)

		elif "UnicodeTranslateError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="UnicodeTranslateError!",
				value="Raised by the sys.exit() function.",
			)
			await message.channel.send(embed=em)

		elif "ValueError" in message.content:
			em = discord.Embed(
				title="Coding Error Detection", description="", color=0x22FC00
			)
			em.add_field(
				name="ValueError!",
				value="Raised when a function or operation is applied to an object of an incorrect type.",
			)
			await message.channel.send(embed=em)

		elif "ZeroDivisionError" in message.content:
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
