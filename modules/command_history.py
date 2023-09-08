# modules/command_history.py

import discord
from config.settings import CHANNEL_ID

client = discord.Client()

class CommandHistory:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        """
        Add a command to the history.
        """
        self.commands.append(command)

    def get_recent_commands(self, count=10):
        """
        Retrieve the most recent 'count' commands.
        """
        return self.commands[-count:]

    async def display_recent_commands(self, channel_id, count=10):
        """
        Send the most recent 'count' commands to the specified Discord channel.
        """
        recent_commands = self.get_recent_commands(count)
        message = "Recent Commands:\n" + "\n".join(recent_commands)
        channel = client.get_channel(channel_id)
        await channel.send(message)

@client.event
async def on_message(message):
    """
    Listen for messages and add commands to the history if they match the command pattern.
    """
    if message.author == client.user:
        return

    # TODO: Match the message content with the command regex pattern. 
    # For the sake of this example, we'll assume all messages are commands.
    command_history.add_command(message.content)

    # If user types '/history', display the recent commands.
    if message.content == '/history':
        await command_history.display_recent_commands(CHANNEL_ID)

if __name__ == "__main__":
    command_history = CommandHistory()
    client.run(DISCORD_API_KEY)
 
