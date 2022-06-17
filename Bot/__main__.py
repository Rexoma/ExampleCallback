import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from Bot.utils import load_plugins
import logging
from telethon import events
from . import innexia

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "Bot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

Innexia = "🎉 Successfully Deployed Deadly InnexiBot 🎉 @ReXomaSupport Enjoy! Do visit @RexomaUpdate"
print(Innexia[0: ])

if __name__ == "__main__":
    innexia.run_until_disconnected()
