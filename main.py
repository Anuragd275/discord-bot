
from discord import Intents, Client, Message
from discord.ext import commands
from responser import get_response

DISCORD_TOKEN = 'YOUR BOT TOKEN'

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("No message")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is up & running!')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    print(f'{username} said: "{user_message}" ({channel})')

    await send_message(message, user_message)


def main() -> None:
    client.run(token=DISCORD_TOKEN)


if __name__ == '__main__':
    main()
