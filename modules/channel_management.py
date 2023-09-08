# modules/channel_management.py

import discord
from config.settings import DISCORD_API_KEY

client = discord.Client()

class ChannelManager:
    def __init__(self, guild):
        self.guild = guild

    async def create_text_channel(self, name):
        """
        Create a new text channel in the guild.
        """
        await self.guild.create_text_channel(name)

    async def create_broadcast_channel(self, name):
        """
        Create a new broadcast (voice) channel in the guild.
        """
        await self.guild.create_voice_channel(name, type=discord.ChannelType.voice)

    @staticmethod
    def recommend_channel_type():
        """
        Based on the requirements, recommend whether a regular channel or a broadcast channel is better.
        For this mock implementation, we'll recommend a text channel.
        """
        return "text_channel"

@client.event
async def on_ready():
    """
    Event triggered when the bot is ready and has logged in.
    """
    print(f'Bot has logged in as {client.user}')
    guild = discord.utils.get(client.guilds)  # Assuming the bot is part of only one guild
    manager = ChannelManager(guild)

    recommended_channel_type = manager.recommend_channel_type()
    if recommended_channel_type == "text_channel":
        await manager.create_text_channel("new-command-channel")
    elif recommended_channel_type == "broadcast_channel":
        await manager.create_broadcast_channel("new-broadcast-channel")

if __name__ == "__main__":
    client.run(DISCORD_API_KEY)
 
