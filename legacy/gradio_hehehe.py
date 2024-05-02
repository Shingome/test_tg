import gradio as gr
import telethon as tel
import json
import asyncio


def command_handler(cmd: str):
    if cmd == "start":
        with open('../channels.json') as ch:
            channels = ch.read()

        with open('../data.json') as d:
            data = d.read()

        channels = json.loads(channels)
        data = json.loads(data)

        # Add loading from file or env
        api_id = data["api_id"]
        api_hash = data["api_hash"]
        # period = data["period"]

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        client = tel.TelegramClient('forward', api_id=api_id, api_hash=api_hash, loop=loop)
        forward_id = data["forward_id"]

        @client.on(tel.events.NewMessage(chats=list(channels.values())))
        async def handler(event):
            if event.message == "Марк, остановись":
                client.disconnect()
            print(f"Send message to {forward_id}. Message = {event.message}")
            await client.forward_messages(forward_id, event.message)

        with client:
            client.run_until_disconnected()

    return "Ok..."


if __name__ == "__main__":
    demo = gr.Interface(fn=command_handler, inputs="text", outputs="text")
    demo.launch()
