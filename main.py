from telethon import TelegramClient, events

api_id = 12345  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API hash
client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello!')

client.start()
client.run_until_disconnected()