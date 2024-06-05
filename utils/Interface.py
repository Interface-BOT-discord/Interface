import pkgutil

import disnake
from disnake.ext import commands


class Interface_Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            intents=disnake.Intents.all(),
            help_command=None
        )

    def load_cog(self, path: str):
        for file in pkgutil.iter_modules([path]):
            try:
                self.load_extension(f'cogs.{file.name}')
                print(f'Loaded {file.name}')
            except Exception as e:
                print(f'Failed to load {file.name} ({type(e).__name__})')