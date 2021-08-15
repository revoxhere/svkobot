import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Netflix"
        )
    )

svko = [
    'Did you know I can terrorize men and women equally',
    'I can tell',
    'Stop pinging me',
    'Use svko help if you need help (but not medical)',
    'YES ITS ME',
    'WHAT DO YOU WANT'
]

svko_hi = [
    'Hey',
    'Wassup',
    'Hello',
    'Hi'
]

help_str = """\
**svkobot by revoxsvko**
Available commands:
    - svko image
    - svko help
"""


@client.event
async def on_message(message):
    mention = f'<@!{client.user.id}>'

    if message.author == client.user:
        return

    if mention in message.content:
        response = random.choice(svko)
        await message.channel.send(response)

    if message.content.startswith("svko hi"):
        response = random.choice(svko_hi)
        await message.channel.send(response)

    if message.content.startswith("svko help"):
        await message.channel.send(help_str)

    if message.content.startswith("svko image"):
        image = os.listdir('responses/')
        imgString = random.choice(image)
        path = 'responses/' + imgString
        await message.channel.send(
            "Random image from **revox's holy archive**:",
            file=discord.File(path)
        )

client.run(TOKEN)
