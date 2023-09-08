# utils/discord_utils.py

import discord

def initialize_bot(token):
    """
    Initialize and run the Discord bot.
    """
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'Bot has logged in as {client.user}')

    client.run(token)
 
