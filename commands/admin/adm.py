import disnake 
from disnake.ext import commands

import json

 

class Adm(commands.Cog):
    def __init__(self, client):
        self.client = client


    # чистить чат
    @commands.command(
        name="очистка",
        
    )
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    # кик 
    @commands.command() 
    async def kick(self, ctx, member : disnake.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention}был кикнут с сервера')

    # бан
    @commands.command()
    async def ban(self, ctx, member : disnake.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} был забанен')

    # разбан
    @commands.command()
    async def unban(self, ctx, *, member ):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.mention}')
                return


    @commands.command()
    async def mute(self, ctx, member = disnake.Member, *, reason=None):
        if(not ctx.author.guild_pressions.manage_messages):
            await ctx.send('This command requires ``Manage Messages``')
            return
        guild = ctx.guild
        muteRole = disnake.utils.get




def setup(client):
    client.add_cog(Adm(client))