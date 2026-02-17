import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Sistema Central Online.")

@bot.command()
async def breach(ctx, scp: str):
    await ctx.send(f"""
[ SISTEMA CENTRAL ]

🚨 ALERTA 🚨
Violação detectada: SCP-{scp}
Todas as unidades devem responder imediatamente.
""")

bot.run(TOKEN)
