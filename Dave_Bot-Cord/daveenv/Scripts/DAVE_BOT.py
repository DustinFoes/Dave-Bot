import discord

intents = discord.Intents.default()
intents.messages.context = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} Is Online')

@client.event
async def on_message(messages):
    if message.author == client.user:
        return

    if message.context.startswith('test'):
        await message.channel.reply('Your Test Worked!')


client.run(OTc0NzEwNTc3ODMyMjg0MTcw.G_ytb6.SZtKGrOVW2Tk0NXdCqqZSXlsWGiko7ZJemOqwk)