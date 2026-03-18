from pyrogram import filters
from vikky import bot
from vikky.utils.filters import owner
import traceback
import io
import sys


# 🧠 async exec
async def aexec(code, client, message):
    exec(
        f'async def __aexec(client, message):\n'
        + '\n'.join(f'    {line}' for line in code.split('\n'))
    )
    return await locals()['__aexec'](client, message)


# 🚀 eval command (.eval / /eval)
@bot.on_message(filters.command("eval", prefixes=[".", "/"]) & owner)
async def eval_handler(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Give some code")

    code = message.text.split(None, 1)[1]

    # capture print output
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()

    try:
        result = await aexec(code, client, message)
        stdout = redirected_output.getvalue()

        output = ""
        if stdout:
            output += stdout
        if result:
            output += str(result)

        if not output:
            output = "✅ Done"

    except Exception:
        output = traceback.format_exc()

    finally:
        sys.stdout = old_stdout

    # split long output
    if len(output) > 4000:
        for i in range(0, len(output), 4000):
            await message.reply(f"```{output[i:i+4000]}```")
    else:
        await message.reply(f"```{output}```")
