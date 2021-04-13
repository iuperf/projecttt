import discord
from discord.ext import commands
import requests
from боты.config import DS_TOKEN

TOKEN = DS_TOKEN

langpair = 'en|ru'

goroskop = 'empty'


class RandomThings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_g')
    async def my_ranint(self, ctx):
        stroka = '\n'.join(['help_g — для инструкций по работе команд бота', 'set_lang — для смены языка',
                            'get_g {дата рождения в формате день-месяц-год} (пример 05-03-2003)'])
        await ctx.send(stroka)

    @commands.command(name='get_g')
    async def roll_dice(self, ctx, date):
        url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
        goroskop = f'Ваш прогноз {date}'  # date заменим на функция(date)
        querystring = {"langpair": langpair, "q": goroskop, "mt": "1", "onlyprivate": "0", "de": "a@b.c"}

        headers = {
            'x-rapidapi-key': "80d3847d95msh4b8b33e90f9d0bdp19e9a5jsn2f560050ea8f",
            'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring).json()
        await ctx.send(response["responseData"]["translatedText"])

    @commands.command(name='set_lang')
    async def my_randint(self, ctx, strok):
        global langpair
        langpair = '|'.join(strok.split('-'))
        await ctx.send('напишите !!текст {ваш текст}')


bot = commands.Bot(command_prefix='!!')
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)