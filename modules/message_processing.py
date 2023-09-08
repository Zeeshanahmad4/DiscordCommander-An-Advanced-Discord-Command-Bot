# modules/message_processing.py

import discord
from config.settings import CHANNEL_ID, REGEX_PATTERN
from modules.command_execution import demo_function
import re

client = discord.Client()

class MessageProcessor:
    def __init__(self):
        pass

    @staticmethod
    def is_command(message_content):
        """
        Check if the message content matches the command regex pattern.
        """
        return re.match(REGEX_PATTERN, message_content)

    async def process_message(self, message_content):
        """
        Process the message content if it's identified as a command.
        """
        if self.is_command(message_content):
            response_type, response_content = await demo_function(message_content)
            return response_type, response_content
        else:
            return None, None

@client.event
async def on_message(message):
    """
    Listen for messages and forward them for processing.
    """
    if message.author == client.user:
        return

    processor = MessageProcessor()
    response_type, response_content = await processor.process_message(message.content)

    # Additional actions based on the response can be implemented here.

if __name__ == "__main__":
    client.run(DISCORD_API_KEY)
 
