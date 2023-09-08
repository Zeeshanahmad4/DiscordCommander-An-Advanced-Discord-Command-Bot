# modules/error_handling.py

import discord
from utils.helpers import custom_logger
from config.settings import CHANNEL_ID

client = discord.Client()

async def log_and_notify_error(channel_id, error_message, error_details=None):
    """
    Log the error and notify users about it in the specified Discord channel.
    """
    custom_logger(f"ERROR: {error_message}")
    if error_details:
        custom_logger(f"DETAILS: {error_details}")

    channel = client.get_channel(channel_id)
    user_friendly_message = f"An error occurred: {error_message}"
    await channel.send(user_friendly_message)

@client.event
async def on_error(event, *args, **kwargs):
    """
    Default event triggered on any error. We override this to handle errors gracefully.
    """
    error_message = f"An unexpected error occurred during the {event} event."
    await log_and_notify_error(CHANNEL_ID, error_message)



if __name__ == "__main__":
    client.run(DISCORD_API_KEY)
 
