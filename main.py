import interactions
from interactions import Button, ButtonStyle, CommandContext, SelectMenu, SelectOption, ActionRow, Modal, TextInput, TextStyleType, Embed
from concurrent.futures import ThreadPoolExecutor
from interactions import (
    extension_listener,
    extension_component,
    Extension,
    Client,
    ComponentContext,
    Message,
    Channel,
    ChannelType,
    File,
    Member,
)
bot = interactions.Client("",intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGES)
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
header = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}
threading = ThreadPoolExecutor(max_workers=int(100000))

@bot.event
async def on_start():
    await bot.change_presence(
        interactions.ClientPresence(activities=[
            interactions.PresenceActivity(
                name="DM me with sms",
                type=interactions.PresenceActivityType.STREAMING)
        ]))

@bot.event
async def on_message_create(message: Message):
    channel = await message.get_channel()
    if channel.type == ChannelType.DM:
        if message.content == "sms":
            start_spam = Button(
                style=ButtonStyle.SUCCESS,
                custom_id="start_sms",
                label="ยิงเบอร์",
            )
            await message.reply(components=[start_spam])


bot.start()