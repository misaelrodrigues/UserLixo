import subprocess

from pyrogram import Client, Filters


@Client.on_message(Filters.command("cmd", prefixes=".") & Filters.me)
async def cmd(client, message):
    text = message.text[5:]
    res = subprocess.getstatusoutput(text)[1] or 'Comando executado'
    await message.edit(res)
