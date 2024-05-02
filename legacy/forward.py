import asyncio
import telethon as tel

# Add loading from file or env
api_id = ""
api_hash = ""
period = 5

client = tel.TelegramClient('test_tg', api_id=api_id, api_hash=api_hash)
# listen_id = client.get_peer_id("Тест")
forward_id = 626133579


@client.on(tel.events.NewMessage(outgoing=True))
async def handler(event):
    await client.forward_messages(forward_id, event.message)

if __name__ == "__main__":
    with client:
        client.run_until_disconnected()