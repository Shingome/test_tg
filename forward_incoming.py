import asyncio
import telethon as tel
import json


with open('channels.json') as ch:
    channels = ch.read()

with open('data.json') as d:
    data = d.read()

channels = json.loads(channels)
data = json.loads(data)

# Add loading from file or env
api_id = data["api_id"]
api_hash = data["api_hash"]
period = data["period"]

client = tel.TelegramClient('forward', api_id=api_id, api_hash=api_hash)
forward_id = 626133579


@client.on(tel.events.NewMessage(chats=list(channels.values())))
async def handler(event):
    await client.forward_messages(forward_id, event.message)

if __name__ == "__main__":
    with client:
        client.run_until_disconnected()