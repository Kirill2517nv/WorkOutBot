import asyncio
import logging

import aiohttp
from aiohttp_socks import ProxyConnector
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession

from config import BOT_TOKEN, PROXY_URL
from database import init_db
from handlers import start, training, stats

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


async def main():
    await init_db()

    if PROXY_URL:
        connector = ProxyConnector.from_url(PROXY_URL)
        http_session = aiohttp.ClientSession(connector=connector)
        session = AiohttpSession()
        session._session = http_session
        bot = Bot(token=BOT_TOKEN, session=session)
        logging.info("Бот запущен через прокси: %s", PROXY_URL)
    else:
        bot = Bot(token=BOT_TOKEN)
        logging.info("Бот запущен без прокси")

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)
    dp.include_router(training.router)
    dp.include_router(stats.router)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
