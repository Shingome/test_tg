import asyncio
import telethon as tel

# Add loading from file or env
api_id = ""
api_hash = ""
period = 5

client = tel.TelegramClient('test_tg', api_id=api_id, api_hash=api_hash)


@client.on(tel.events.NewMessage(outgoing=True))
async def handler(event):
    await asyncio.sleep(period)
    await client.delete_messages(event.chat_id, event.id)

if __name__ == "__main__":
    with client:
        client.run_until_disconnected()