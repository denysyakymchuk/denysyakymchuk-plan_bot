from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5052103879:AAHKs5um-TrxSfVcn01T8DJfGtTXdOS00CA'
port = 8080

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())