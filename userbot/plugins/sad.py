from ..utils import admin_cmd ,sudo_cmd,edit_or_reply
import asyncio

@borg.on(admin_cmd(pattern="sed$"))
@borg.on(sudo_cmd(pattern="sed$",allow_sudo=True))
async def _(event):
    event = await edit_or_reply(event,"Why you make me sed sir 😭")
    await asyncio.sleep(0.7)
    strings = [
        "•́  ‿ ,•̀",
            "ಥ‿ಥ",
            "ʕ´• ᴥ•̥ʔ",
            "(╯︵╰,)",
            "( ；∀；)",
            "(´；ω；｀)",
            "(･ัω･ั)",
            "(╯︵╰,)",
            "Ó╭╮Ò",
            "(っ˘̩╭╮˘̩)っ",
            "( ･ั﹏･ั)",
            "(｡ŏ﹏ŏ)",
            "(๑´•.̫ • ๑)",
            "(´ . .̫ . )",
            "(｡•́︿•̀｡)",
            "(｡ﾉω＼｡)",
            "ಥ╭╮ಥ",
            "(ᗒᗩᗕ)",
            "( ≧Д≦)",
            ".·´¯(>▂<)´¯·.",
            "( ⚈̥̥⌢⚈̥̥)",
            "ಥ_ಥ",
            "(´;︵;)",
            "༼;´༎ຶ ۝ ༎ຶ༽",
            "｡:ﾟ(;´∩`;)ﾟ:｡",
            "(༎ຶ ෴ ༎ຶ)",
            "( ꈨຶ ˙̫̮ ꈨຶ )",
            "(〒﹏〒)",
            "(个_个)",
            "(╥﹏╥)",
            "(-̩̩-̩̩-̩̩-̩̩-̩̩___-̩̩-̩̩-̩̩-̩̩-̩̩)",
            "(´°̥̥ω°̥̥｀)"
]
    for i in range(0,31):
        await asyncio.sleep(0.7)
        await event.edit(strings[i])