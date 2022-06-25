import requests
import disnake
from disnake.ext import commands
import json

class Activities(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def youtube(self, ctx):
        embed = disnake.Embed()
        data = {
            "max_age": 0,
            "max_users": 0,
            "target_application_id": "880218394199220334",
            "target_type": 2,
            "tempora": False,
            "validate": None
        }
        headers = {
            "Authorization": "Bot OTMxMjA2NTM0MTQ1NDA0OTQ4.YeBDqg.ZSS2RLXfQ_3HD2XsdZMlg7EYxyw",
            "Content-Type": "application/json"
        }

        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                embed.add_field(name="Зайдите в канал", value="2")
                await ctx.send(embed=embed)
        else:
            await ctx.send("Зайдите в канал")

        response = requests.post(
            f"https://disnake.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)

        await ctx.send(f"https://disnake.com/invite/{link['code']}")

    @commands.command()
    async def chess(self, ctx):
        data = {
            "max_age": 0,
            "max_users": 0,
            "target_application_id": "832012774040141894",
            "target_type": 2,
            "tempora": False,
            "validate": None
        }
        headers = {
            "Authorization": "Bot OTMxMjA2NTM0MTQ1NDA0OTQ4.YeBDqg.ZSS2RLXfQ_3HD2XsdZMlg7EYxyw",
            "Content-Type": "application/json"
        }

        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("Зайдите в канал")
        else:
            await ctx.send("Зайдите в канал")

        response = requests.post(
            f"https://disnake.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)

        await ctx.send(f"https://disnake.com/invite/{link['code']}")

    @commands.command()
    async def poker(self, ctx):
        data = {
            "max_age": 0,
            "max_users": 0,
            "target_application_id": "755827207812677713",
            "target_type": 2,
            "tempora": False,
            "validate": None
        }
        headers = {
            "Authorization": "Bot OTMxMjA2NTM0MTQ1NDA0OTQ4.YeBDqg.ZSS2RLXfQ_3HD2XsdZMlg7EYxyw",
            "Content-Type": "application/json"
        }

        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("Зайдите в канал")
        else:
            await ctx.send("Зайдите в канал")

        response = requests.post(
            f"https://nexcord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)

        await ctx.send(f"https://nexcord.com/invite/{link['code']}")


def setup(client):
    client.add_cog(Activities(client))
