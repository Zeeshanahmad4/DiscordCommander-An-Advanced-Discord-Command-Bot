# main.py

import discord
from config.settings import DISCORD_API_KEY
from modules.user_management import UserManagement
from modules.channel_management import create_channel
from modules.command_execution import demo_function
from modules.response_posting import post_text_response, post_image_response, post_link_response
from modules.error_handling import log_and_notify_error
from modules.command_history import CommandHistory
import re

client = discord.Client()

user_manager = UserManagement(DISCORD_API_KEY)
command_history = CommandHistory()

@client.event
async def on_ready():
    """
    Event triggered when the bot is ready and has logged in.
    """
    print(f'Bot has logged in as {client.user}')

@client.event
async def on_message(message):
    """
    Listen for messages and process user interactions.
    """
    if message.author == client.user:
        return

    # Check if the message matches the command regex pattern
    if re.match(REGEX_PATTERN, message.content):
        command_history.add_command(message.content)
        
        response_type, response_content = await demo_function(message.content)
        
        # Based on the response type, post the appropriate response to the Discord channel
        if response_type == "text":
            await post_text_response(CHANNEL_ID, response_content)
        elif response_type == "image":
            await post_image_response(CHANNEL_ID, response_content)
        elif response_type == "link":
            await post_link_response(CHANNEL_ID, response_content)

    # Check for special commands, like '/history'
    if message.content == '/history':
        await command_history.display_recent_commands(CHANNEL_ID)

if __name__ == "__main__":
    client.run(DISCORD_API_KEY)
 
