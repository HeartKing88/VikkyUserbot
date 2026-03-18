from pyrogram import filters
from vikky import bot
from vikky.utils.filters import owner
import traceback

async def aexec(code, client, message):
    exec(
        f'async def __aexec(client, message):\n'
        + '\n'.join(f'    {line}' for line in code.split('\n'))
    )
    return await locals()['__aexec'](client, message)

@bot.on_message(filters.command("eval") & owner)
async def eval_handler(client, message):
    if len(message.command) < 2:
        return await message.reply("Give code")

    code = message.text.split(None, 1)[1]

    try:
        result = await aexec(code, client, message)
        output = str(result) if result else "Done"
    except Exception as e:
        output = "".join(traceback.format_exception(type(e), e, e.__traceback__))

    await message.reply(output[:4000])
