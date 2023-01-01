import discord
from discord import Intents, Message
from typing import Any, Optional


class DiscordBot(discord.Client):
    skills: dict = {}
    allowed: list = []
    trigger: None | str = None

    def __init__(self, *, intents: Optional[Intents] = None, trigger: str,  **options: Any):
        if intents:
            super().__init__(intents=intents, **options)
        else:
            intents = Intents.default()
            intents.message_content = True
            super().__init__(intents=intents, **options)

        self.trigger = trigger

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: Message) -> None:
        if message.author == self.user:
            return

        if self.trigger in message.content and self.trigger is not None:
            skill = message.content.replace(self.trigger, "")
            f = self.skills.get(skill)
            await message.channel.send(f())

    def add_skill(self, name, function):
        self.skills[name] = function

    def show_skills(self):
        return str(self.skills)

    def add_allowed_user(self, username):
        self.allowed.append(username)

    def show_allowed_users(self):
        return str(self.allowed)