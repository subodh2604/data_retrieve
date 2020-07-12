from telethon.sync import TelegramClient,events
import configparser
from telethon import utils

config = configparser.ConfigParser()
config.read("config-sample.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

with TelegramClient(username,api_id,api_hash) as client:
    messages=client.get_messages('https://t.me/botcurrent',limit=10000)
    print("messages no: ",len(messages))
    count=0
    required_files=0
    exception_count=0
    for msg in messages:
        count+=1
        try:
            pdf_name=msg.media.document.attributes[0].file_name
        except:
            exception_count+=1
            continue
        
        client.download_media(msg)
 

