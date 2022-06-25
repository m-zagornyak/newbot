
import disnake
from disnake.ext import commands

from random import randint
from random import random

from lib import database

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.db = database.DataBase()


    @commands.command(
        name="баланс",
		aliases=["cash", "balance"],
		brief="Вывод баланса пользователя",
		usage="balance <@user>"
    )
    async def balance(self, ctx, member: disnake.Member=None):
        balance = await self.db.get_data(ctx.author)
        embed = disnake.Embed(
			description=f"Баланса пользователя __{ctx.author}__: **{balance['balance']}**"
		)

        if member is not None:
            balance = await self.db.get_data(member)
            embed.description = f"Баланса пользователя __{member}__: **{balance['balance']}**"
            await ctx.send(embed=embed)


    @commands.command(
		name="перевод",
		aliases=["give-cash", "givecash", "pay"],
		brief="Перевод денег другому пользователю",
		usage="pay <@user> <amount>"
	)
    async def pay_cash(self, ctx, member: disnake.Member, amount: int):
        balance = await self.db.get_data(ctx.author)
        embed = disnake.Embed()

        if member.id == ctx.author.id:
            embed.description = f"__{ctx.author}__, конечно извините меня, но проход жучкам сегодня закрыт."

        if amount <= 0:
            embed.description = f"__{ctx.author}__, конечно извините меня, но проход жучкам сегодня закрыт."
        elif balance["balance"] <= 0:
            embed.description = f"__{ctx.author}__, недостаточно средств"
        else:
            await self.db.update_member(ctx.author, {"$inc": {"balance": -amount}})
            await self.db.update_member(member, {"$inc": {"balance": amount}})

            embed.description = f"__{ctx.author}__, транзакция прошла успешно"

            await ctx.send(embed=embed)
           
            
    @commands.command(
        name="казино",
        aliases=["casino"],
        brief="Если больше число которые ты написал то ты выиграл",
        usage="casino <amount>"
    )
    async def casino(self, ctx, member: disnake.Member, amount):

        balance = await self.db.get_data(ctx.author)
        embed = disnake.Embed()
        
        factor = 4
        
        fullLoss = random.random() < 0.25
        win = randint(amount, factor * amount)
        
        summery = 0 if fullLoss else win
        
        self.db.update_member({"member.id": member.id}, {"$set": {"balance": balance + summery}})
        
        embed.description = f"__{ctx.author}__, транзакция прошла успешно"
        await ctx.send(embed=embed)
        
 
    
    @commands.command(
        name="работа",
        aliases=["work"],
        brief="Получаешь деньги каждие 5 часов",
        usage="work <user>"
    )
    async def work(self, ctx, member: disnake.Member, amount: 40):
        embed = disnake.Embed()
        
        if member.id == ctx.author.id:
            await self.db.update_member(member, {"$inc": {"balance": amount}})
            embed.description = f"__{ctx.author}__, вы заработали "
            
        
        


def setup(client):
    client.add_cog(Economy(client))