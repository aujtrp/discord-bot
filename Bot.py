import os
import discord
from discord.ext import commands

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="?", intents=intents)


@bot.event
async def setup_hook():
    await bot.tree.sync()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def join(ctx):
    if ctx.author.voice:
        if ctx.voice_client:
            await ctx.voice_client.move_to(ctx.author.voice.channel)
        else:
            await ctx.author.voice.channel.connect()
        await ctx.send("دخلت للروم ✅")
    else:
        await ctx.send("ادخل لروم صوتي أولاً")


@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("خرجت 👋")


@bot.tree.command(name="ping", description="Test the bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")


bot.run(TOKEN)


