import os
import discord
import random
import scrapetube
from time import sleep
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
]

number_list = [
    'you think you\'re funny?',
    'well it\'s not 1999 so you cant break the system with that',
    'fuck off with these "numbers"',
    'provide a valid number you idiot',
    'that is not a valid number',
    'are you dumb or am i too advanced for you',
    'i need a n-u-m-b-e-r, not this... thing'
]

svko_hi = [
    'hey',
    'yo',
    'wassup',
    'hello',
    'hi'
]

svko_about = [
    ':eyes:',
    'me?',
    'its me',
    'kiss kiss'
]

svko_ask = [
    '?',
    '??',
    'wtf?',
    'wtf',
    'ikr?'
]

svko_xd = [
    'X D',
    'XD',
    'XDD',
    'XDDD',
    'XDDDD',
    'XXDDDd',
    'bruh'
]

svko_gen = [
    'agree',
    'what',
    'ok',
    'same',
    'true',
    'nope',
]

help_str = """\
**svkobot by revoxsvko**
Available commands:
    - svko image [optional id]
    - svko help
    - svko video:
        - przygody
        - revox
        - revox2
        - revox3
"""

revox_videos = []
revox = scrapetube.get_channel("UCgqCK9yt-ajwi4XBu4-jIvA")
for video in revox:
    revox_videos.append(video)

revox2_videos = []
revox2 = scrapetube.get_channel("UCiqkZT-vhW1bLl4uJI3sSfQ")
for video in revox2:
    revox2_videos.append(video)

revox3_videos = []
revox3 = scrapetube.get_channel("UC3jLSu6yMmJbKzKXpWQGmxA")
for video in revox3:
    revox3_videos.append(video)

przygody_videos = []
przygody = scrapetube.get_playlist("PL0nttajE9zQGOsryzY8Yv3GpnKE9u9ZSF")
for video in przygody:
    przygody_videos.append(video)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(client.user.id).lower() in message.content.lower():
        response = random.choice(svko)
        await message.channel.send(
            f"{message.author.mention}, {response}")

    if message.content in svko_gen:
        response = random.choice(svko_gen)
        await message.channel.send(response)

    if message.content in svko_ask:
        response = random.choice(svko_ask)
        await message.channel.send(response)

    if message.content in svko_xd:
        response = random.choice(svko_xd)
        await message.channel.send(response)

    if message.content in svko_hi:
        response = random.choice(svko_hi)
        await message.channel.send(response)

    if message.content.lower().startswith("svko"):
        command = message.content.lower().replace("svko ", "").split(" ")

        if command[0] == "avatar":
            if message.author.guild_permissions.administrator:
                try:
                    avatar_path = "avatars/" + \
                        random.choice(os.listdir('avatars/'))
                    avatar = open(avatar_path, 'rb').read()
                    await client.user.edit(avatar=avatar)
                    await message.channel.send("Changed avatar!", file=discord.File(avatar_path))
                except Exception as e:
                    await message.channel.send(f"Error changing avatar: {e}")
            else:
                await message.channel.send("You're not an administrator!")

        elif command[0] == "video":
            if len(command) > 1:
                if str(command[1]) == "przygody":
                    text = "Here's your random **przygody revoxa w świecie CS:GO** video: "
                    text += f"https://youtu.be/{random.choice(przygody_videos)['videoId']}"
                    await message.channel.send(text)
                elif str(command[1]) == "revox3":
                    text = "Here's your random **revox3** video: "
                    text += f"https://youtu.be/{random.choice(revox3_videos)['videoId']}"
                    await message.channel.send(text)
                elif str(command[1]) == "revox2":
                    text = "Here's your random **revox2** video: "
                    text += f"https://youtu.be/{random.choice(revox2_videos)['videoId']}"
                    await message.channel.send(text)
                elif str(command[1]) == "revox":
                    text = "Here's your random **revox** video: "
                    text += f"https://youtu.be/{random.choice(revox_videos)['videoId']}"
                    await message.channel.send(text)
                else:
                    await message.channel.send("Usage: `svko video [przygody, revox, revox2, revox3]`")
            else:
                await message.channel.send("Usage: `svko video [przygody, revox, revox2, revox3]`")

        elif command[0] == "help":
            await message.channel.send(help_str)

        elif command[0] == "image":
            with message.channel.typing():
                image = os.listdir('responses/')

                if len(command) > 1:
                    try:
                        user_num = int(command[1])

                        if user_num <= 0:
                            await message.channel.send(random.choice(number_list))
                            return

                        elif len(image) < user_num:
                            await message.channel.send(
                                f"i have like {len(image)} holy screenshots, not {user_num}")
                            return

                        path = 'responses/' + image[user_num-1]
                        await message.channel.send(
                            "image *#" +
                            str(command[1])+"* from **revox's holy archive**:",
                            file=discord.File(path))
                    except Exception as e:
                        print(e)
                        await message.channel.send(random.choice(number_list))
                        return
                else:
                    random_num = random.randint(0, len(image)-1)
                    path = 'responses/' + image[random_num]

                    await message.channel.send(
                        "random image *(#"+str(random_num) +
                        ")* from **revox's holy archive**:",
                        file=discord.File(path))

    elif 'svko' in message.content.lower():
        response = random.choice(svko_about)
        await message.channel.send(response)

client.run(TOKEN)
