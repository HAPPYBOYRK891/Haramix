from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("💥𝐂𝐎𝐌𝐌𝐀𝐌𝐃𝐒💥", data="help_back")
    ],
    [
        Button.url("☠𝐃𝐀𝐃𝐃𝐘☠", "https://t.me/HAPPY_BOT_RK"),
        Button.url("🔥𝐒𝐔𝐏𝐏𝐎𝐑𝐓🔥", "https://t.me/ll_DPZ_W0RLD_ll")
    ],
    [
        Button.url("👻𝐂𝐇𝐀𝐍𝐍𝐄𝐋👻", "https://t.me/style_names")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/e63eff085fabb2fe2c845.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
