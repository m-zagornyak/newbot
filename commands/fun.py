import disnake
import random
import giphy_client
from random import choice
from disnake.ext import commands
from giphy_client.rest import ApiException



class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx, *, q="Smile"):
        api_key = 'ho60Peymnk6iNpizcl9FU6j5Xyw9FHwM'
        api_instance = giphy_client.DefaultApi()

        try:
            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff =random.choice(lst)

            await ctx.channel.send(giff.embed_url)

        except ApiException as e:
            print("Exception when calling App")


    @commands.slash_command()
    async def gif(self, ctx, *, q="Smile"):
      api_key = 'ho60Peymnk6iNpizcl9FU6j5Xyw9FHwM'
      api_instance = giphy_client.DefaultApi()

      try:
          api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
          lst = list(api_response.data)
          giff =random.choice(lst)

          await ctx.channel.send(giff.embed_url)

      except ApiException as e:
          print("Exception when calling App")


def setup(client):
    client.add_cog(Fun(client))


