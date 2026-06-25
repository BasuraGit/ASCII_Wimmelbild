import asyncio
from util.Enums import ErfolgsEnum

class Timer:
    async def start(self, timer_max, timer_label , app):
        for time in range(timer_max, 0, -1):
            timer_label.text = f"Zeit: 00:{time:02d}"
            app.invalidate()
            await asyncio.sleep(1)
        return ErfolgsEnum.TIMEOUT

