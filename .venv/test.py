import discord


TOKEN = "MTI4Nzg1ODcyOTE5NDA5ODg3MQ.GBoa_G.0SLNdIj4ddq-kMwlqY5jWJmQDfOt79cdR0YX7Y"
CHANNEL_ID = int(1287858067299369041)


class Client(discord.Client):
    async def on_ready(self):
        print(f"the bot {self.user} logged in")

        channel = await self.fetch_channel(CHANNEL_ID)
        await channel.send("this bot just logged in")


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)