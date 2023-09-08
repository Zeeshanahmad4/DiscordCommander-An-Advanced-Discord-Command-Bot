# modules/command_execution.py

import discord
from config.settings import CHANNEL_ID, REGEX_PATTERN
from modules.response_posting import post_text_response, post_image_response, post_link_response
import re
import asyncio

client = discord.Client()

# Placeholder function for demo purposes
async def demo_function(command):
    # Here, you can process the command and return an appropriate response.
    # This is just a mock function for demonstration.
    if "text" in command:
        return "text", "This is a text response."
    elif "image" in command:
        return "image", "path_to_image.jpg"  # Replace with an actual image path or URL
    elif "link" in command:
        return "link", "https://example.com"
    else:
        return "text", "Unknown command."

@client.event
async def on_message(message):
    """
    Listen for messages and process commands if they match the command pattern.
    """
    if message.author == client.user:
        return

    # Check if the message matches the command regex pattern
    if re.match(REGEX_PATTERN, message.content):
        response_type, response_content = await demo_function(message.content)
        
        # Based on the response type, call the appropriate response posting function
        if response_type == "text":
            await post_text_response(CHANNEL_ID, response_content)
        elif response_type == "image":
            await post_image_response(CHANNEL_ID, response_content)
        elif response_type == "link":
            await post_link_response(CHANNEL_ID, response_content)

if __name__ == "__main__":
    client.run(DISCORD_API_KEY)
 
