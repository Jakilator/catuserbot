#By Parrot @i_am_no_one_0_0
#https://t.me/i_am_no_one_0_0
from ..utils import admin_cmd ,sudo_cmd,edit_or_reply
import asyncio

@borg.on(admin_cmd(pattern="bomb$"))
@borg.on(sudo_cmd(pattern="bomb$",allow_sudo=True))
async def _(event):
    event = await edit_or_reply(event,"The Bomb Has Been Triggred 😈")
    await asyncio.sleep(0.7)
    strings = ["00:20•••••••••••••••••••🧨","00:19••••••••••••••••••🧨","00:18•••••••••••••••••🧨","00:17••••••••••••••••🧨","00:16•••••••••••••••🧨","00:15••••••••••••••🧨","00:14•••••••••••••🧨","00:13••••••••••••🧨","00:12•••••••••••🧨","00:11••••••••••🧨","00:10•••••••••🧨","00:09••••••••🧨","00:08•••••••🧨","00:07••••••🧨","00:06•••••🧨","00:05••••🧨","00:04••••🧨","🟥🟥🟥💣","🟥🟥💣","🟥💣","💣"]
    for i in range(0,21):
    	await asyncio.sleep(1.0)
    	await event.edit(strings[i])
    await asyncio.sleep(1.0) 
    await event.edit("Boooooooooommmm!!!")
    bum = ["💥","💥💥💥","💥💥💥💥💥"," 💥💥💥💥💥💥💥","💥💥💥💥💥💥💥💥💥"," 💥💥💥💥💥💥💥💥💥💥💥","💥💥💥💥💥💥💥💥💥💥💥","💥💥💥💥💥💥💥💥💥","💥💥💥💥💥💥💥"," 💥💥💥💥💥","💥💥💥"," 💥","You😈🤯🤯🤯😈Ded"
    ]
    for i in range(0,13):
    	await asyncio.sleep(0.6)
    	await event.edit(bum[i])