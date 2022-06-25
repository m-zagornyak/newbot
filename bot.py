
from traceback import format_exc
from loguru import logger as Logger
from services import Module

from disnake_components import Button
import disnake
from disnake.ext import commands
from configs.config import *


client = commands.Bot(command_prefix = Config.prefix,  intents = disnake.Intents().all())

client.remove_command("help")

    
@client.command(aliases=['load', 'подгрузить'])
@commands.is_owner()
async def _load(ctx, cog: str=None):
    if cog is None: emd = disnake.Embed(title = 'Ошибка', description = 'Вы не указали ког')
    else:
        try:
            client.load_extension(f'cogs.{cog}')
            emb = disnake.Embed(title = 'Ког', description = f'Ког {cog} был успешно загружен', color = 0xFF7F50)
        except Exception as e: return await ctx.reply(embed = disnake.Embed(title = 'Ошибка', description = f'Не найден ког {cog}', color = 0xff0000))
    return await ctx.reply(embed=emd)


@client.command(aliases=['unload', 'отгрузить'])
@commands.is_owner()
async def _unload(ctx, cog: str=None):   
    if cog is None: emd = disnake.Embed(title = 'Ошибка', description = 'Вы не указали ког')
    else:
        try:
            client.unload_extension(f'cogs.{cog}')
            emd = disnake.Embed(title = 'Ког', description = f'Ког {cog} был успешно отгружен', color = 0xFF7F50)
        except Exception as e: return await ctx.reply(embed = disnake.Embed(title = 'Ошибка', description = f'Не найден ког {cog}', color = 0xff0000))
    return await ctx.reply(embed=emd)


@client.command(aliases=['reload', 'перегрузить', 'перезапустить'])
@commands.is_owner()
async def _reload(ctx, cog: str=None):
    if cog is None: emd = disnake.Embed(title = 'Ошибка', description = 'Вы не указали ког')
    else:
        try:
            client.unload_extension(f'cogs.{cog}')
            client.load_extension(f'cogs.{cog}')
            embed = disnake.Embed(title='Ког', description=f'Ког {cog} был успешно перезагружен', color=0xFF7F50)
        except Exception as e: return await ctx.reply(embed=disnake.Embed(title='Ошибка', description=f'Не найден ког {cog}', color = 0xff0000))
    return await ctx.reply(embed=embed)

# + load all cogs

extensions = [
    './commands/**/*.py'
    
]


def load_modules(self):
    Logger.info('Loading extensions...')
    loaded = 0
    total  = 0
    for extension in extensions:
        if extension.startswith('./'):
            for filename in glob(extension, recursive=True):
                if '__init__' in filename:
                    continue # Skip __init__ files
                total += 1
                try:
                    self.load_extension(Module(path=filename).id)
                except:
                    Logger.error(f'Error when loading extension {filename}:\n{format_exc()}')
                else:
                    loaded += 1
            
        else:
            total += 1
            try:
                self.load_extension(extension)
            except:
                Logger.error(f'Error when loading extension {extension}:\n{format_exc()}')
            else:
                loaded += 1

    Logger.success(f'Loaded {loaded} of {total} extensions')


load_modules(client) 

client.run(Config.token)
