import disnake
from disnake.ext import commands
from disnake_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name="Информация о боте",
        aliases=["help", "bothelp"],
        brief="Информация о Командах бота",
        usage="help"
    )
    async def hhelp(self, ctx):
        embed = disnake.Embed(title="help", description="Кoманда help показивает команды", color=0x000000)
        embed.add_field(name="info", value="`serverinfo`, `help`")
        embed.add_field(name="Activities", value="`poker`, `youtube`, `chess`")
            
        await ctx.send(embed=embed)
        
        
    @commands.command(
        name="Сервер инфо",
        aliases=["serverinfo", "server"],
        brief="Информация о сервере",
        usage="serverinfo"
    )
    async def serverinfo(self, ctx):
        role_cound = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

        embed = disnake.Embed(
            timestamp=ctx.message.created_at, color=ctx.author.color)
        
        embed.add_field(
            name='Name', value=f"{ctx.guild.name}", inline=False)
        embed.add_field(
            name='Member Count', value=ctx.guild.member_count, inline=False)
        embed.add_field(name='Verification Level', value=str(
            ctx.guild.verification_level), inline=False)
        embed.add_field(
            name='Number of Roles', value=str(role_cound), inline=False)
        embed.add_field(
            name='Bot', value=','.join(list_of_bots), inline=False)

        await ctx.send(embed=embed)
        
        
    @commands.command()
    async def select(self, ctx):
        
        embed = disnake.Embed(title="Привет", description="Вот все мои категории", color=0x000000)
        embed.add_field(name="Info", value="Voice", inline=False)
        embed.add_field(name="Game", value="Music", inline=False)
        embed.add_field(name="User", value="Admin", inline=True)

        
        await ctx.send(
            embed=embed,
            components=[
                Select(
                    placeholder="Выберете категорию",
                    options=[
                        SelectOption(label="Info", value="[13]"),
                        SelectOption(label="Voice", value="b"),
                        SelectOption(label="Game", value="a")
                    ],
                    custom_id="select1",
                )
            ],
            )

    
def setup(client):
    client.add_cog(Help(client))
