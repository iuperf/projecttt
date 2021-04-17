from discord.ext import commands
import requests
from боты.config import DS_TOKEN

TOKEN = DS_TOKEN


goroskop = 'empty'


class RandomThings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_g')
    async def my_ranint(self, ctx):
        stroka = '\n'.join(['help_g — для инструкций по работе команд бота',
                            'get_g {дата рождения в формате день-месяц-год} (пример 05-03-2003)'])
        await ctx.send(stroka)

    @commands.command(name='get_g')
    async def roll_dice(self, ctx, date):
        goroskop = f'Ваш прогноз {date}'  # date заменим на функция(date)
        await ctx.send(goroskop)




bot = commands.Bot(command_prefix='!!')
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)