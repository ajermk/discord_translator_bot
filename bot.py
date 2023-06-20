import discord

from translator import Translator

class Bot(discord.Bot):

    async def on_ready(self):
        print('Logged in as:')
        print(self.user.name)
        print('-------')

    async def on_message(self,message):
        if message.author == self.user:
            return
        translated = Translator().translate(message.content)
        if translated:
            if translated.startswith("Quota exceeded"):
                await message.channel.send(translated)
                await self.close()
                if self.is_closed():
                    return
            await message.reply(translated)

    @discord.slash_command()
    async def test(self, ctx):
        await ctx.channel.send("hello")


