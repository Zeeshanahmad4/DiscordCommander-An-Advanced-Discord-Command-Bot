# modules/response_posting.py

import discord
from config.settings import DISCORD_API_KEY, CHANNEL_ID

client = discord.Client()

async def post_text_response(channel_id, message_content):
    """
    Post a text message to the specified Discord channel.
    """
    channel = client.get_channel(channel_id)
    await channel.send(message_content)

async def post_image_response(channel_id, image_url):
    """
    Post an image to the specified Discord channel using an image URL.
    """
    channel = client.get_channel(channel_id)
    await channel.send(file=discord.File(image_url))

async def post_link_response(channel_id, link):
    """
    Post a link to the specified Discord channel.
    """
    channel = client.get_channel(channel_id)
    await channel.send(link)

async def post_combined_response(channel_id, message_content, image_url, link):
    """
    Post a combination of text, image, and link to the specified Discord channel.
    """
    channel = client.get_channel(channel_id)
    combined_message = f"{message_content}\n{link}"
    await channel.send(content=combined_message, file=discord.File(image_url))



if __name__ == "__main__":
    client.run(DISCORD_API_KEY)
 
