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
    'did you know I can terrorize men and women equally',
    'mhm',
    'amazing',
    'i can tell',
    'stop pinging me',
    'use svko help if you need help (but not medical)',
    'yo',
    '?',
    '??',
    'X D'
]

svko_hi = [
    'hey',
    'yo',
    'wassup',
    'hello',
    'hi'
]

help_str = """\
**svkobot by revoxsvko**
Available commands:
    - svko image
    - svko help
"""


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mention = f'<@!{client.user.id}>'
    if mention in message.content:
        response = random.choice(svko)
        await message.channel.send(
            message.author.mention
            + ", "
            + response)

    if message.content.startswith("svko"):
        command = message.content.strip("svko ").split(" ")

        if command[0].lower() in svko_hi:
            response = random.choice(svko_hi)
            await message.channel.send(response)

        if command[0].lower() == "help":
            await message.channel.send(help_str)

        if command[0].lower() == "image":
            image = os.listdir('responses/')
            imgString = random.choice(image)
            path = 'responses/' + imgString
            await message.channel.send(
                "Random image from **revox's holy archive**:",
                file=discord.File(path))

client.run(TOKEN)
