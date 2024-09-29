from gpt_discord_client import client

import threading
import random
import string
import os

from typing import Dict
from dotenv import load_dotenv

load_dotenv()

client = client(os.getenv('token'), gpt_style='You are very smart!')

@client.event
def on_message(message: Dict):

    # if user's message
    if message['t'] == 'MESSAGE_CREATE':
        
        # if a bot is mentioned in the message and not bot's message
        if any(i['id'] == client._discord_http_client.client_id for i in message['d']['mentions']) and message['d']['author']['id'] != client._discord_http_client.client_id:

            message['d']['content'] = message['d']['content'].replace(f'<@{client._discord_http_client.client_id}>', '')

            print(f"@{message['d']['author']['username']}: {message['d']['content'].lstrip()}")
          
            # content: say Im cool bot -> voice message "Im cool bot"
            if message['d']['content'].lstrip().startswith('say') and len(message['d']['content']) > 3:

                threading.Thread(target=client.reply_with_voice_message, args=[
                            message['d']['content'][4:],
                            message['d']['id'],
                            message['d']['channel_id'],
                            message['d']['guild_id'],
                            f'voice{"".join(random.choices(string.ascii_letters, k=5))}.mp3',
                            True
                        ]).start()
            
            # content: gpt 2 + 2 -> gpt answer "2 + 2 is 4, bro"
            elif message['d']['content'].lstrip().startswith('gpt') and len(message['d']['content']) > 3:

                        threading.Thread(target=client.reply_with_gpt, args=[
                            message['d']['content'][4:], 
                            message['d']['id'], 
                            message['d']['channel_id'], 
                            message['d']['guild_id']
                        ]).start()
