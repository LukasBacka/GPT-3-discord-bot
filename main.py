import openai
import discord

client = discord.Client(intents=discord.Intents.default())

# Add your OpenAI API key here
openai.api_key = "YOUR_API_KEY"

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/chat"):
        if "gpt" in [role.name for role in message.author.roles]:
            prompt = message.content[6:]
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=0.7,
            )
            await message.channel.send(response.choices[0].text)
        else:
            await message.channel.send("You do not have the proper role to use this command.")

client.run("YOUR_DISCORD_BOT_TOKEN")
