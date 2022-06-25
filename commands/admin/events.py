import disnake
from disnake.ext import commands

from lib import database
    
class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.db = database.DataBase()


    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.client.guilds:
            for member in guild.members:
                await self.db.insert_new_member(member)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.db.insert_new_member(member)
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Бот готов")
        
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: disnake.Member, before: disnake.VoiceState, after: disnake.VoiceState):
        if member.bot:
            return
        
        if not before.channel:
            print(f"{member.name}")
            
        if before.channel and not after.channel:
            print("User left chhanel")
        



def setup(client):
    client.add_cog(Events(client))
