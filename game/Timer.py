import asyncio
from util.Enums import ErfolgsEnum
from prompt_toolkit.application import Application as app
from prompt_toolkit.widgets import Label

class Timer:
    async def start(
        self,
        timer_max: int, 
        timer_label: Label, 
        app: app
    ):
        
        for time in range(timer_max, -1, -1):
            timer_label.text = f"Zeit: 00:{time:02d}"
            app.invalidate()
            await asyncio.sleep(1)
        return ErfolgsEnum.TIMEOUT

