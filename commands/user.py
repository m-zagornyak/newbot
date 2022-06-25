import disnake
from disnake.ext import commands
from disnake_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)

class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatar(self, ctx, member: disnake.Member = None):
        if member == None:
            member = ctx.author

        memberAvatar = member.avatar

        embed = disnake.Embed(title=f"{member.name} Avatar")
        embed.set_image(url=memberAvatar)

        await ctx.send(embed=embed)
        
        
    @commands.command()
    async def button(self, ctx):
        async def callback(self, interaction):
            await interaction.send(content="Yay")

        await ctx.send(
            "Button callbacks!",
            components=[
                    Button(style=ButtonStyle.blue, label="Click this"), callback
            ],
        )


def setup(client):
    client.add_cog(User(client))
