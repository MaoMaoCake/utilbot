import os
from dotenv import load_dotenv
from skills import get_ip
from bot import DiscordBot
load_dotenv()

client = DiscordBot(trigger="!")

client.add_skill("ip", get_ip)

client.run(os.getenv("BOT_SECRET"))
