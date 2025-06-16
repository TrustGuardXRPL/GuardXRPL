
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("API_TOKEN") or "7115580006:AAH9Y_bOy0WW_zgX3gkCbKStwTRtGuTQUGQ"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'about'])
async def send_welcome(message: Message):
    await message.reply(
        "🛡️ Welcome to TrustGuard XRPL Bot!\n\n"
        "Use /check [token] to investigate XRPL tokens.\n"
        "Use /scan [wallet] to scan wallets.\n"
        "Report scams with /report [token]."
    )

@dp.message_handler(commands=['check'])
async def check_token(message: Message):
    args = message.get_args()
    if not args:
        await message.reply("❗ Please provide a token name. Example: /check DOGE")
        return
    token = args.upper()
    # Симулируем проверку токена (можно подключить xrpl-py)
    await message.reply(f"🔍 Checking token `{token}` on XRPL...\n\n⚠️ Fake data: Trustlines: 5, Volume: 120K XRP.")

@dp.message_handler(commands=['scan'])
async def scan_wallet(message: Message):
    address = message.get_args()
    if not address:
        await message.reply("❗ Please provide a wallet address. Example: /scan rXXXXXXX")
        return
    await message.reply(f"📊 Scanning wallet `{address}`...\n\n🧪 Found 3 suspicious tokens.")

@dp.message_handler(commands=['report'])
async def report_token(message: Message):
    token = message.get_args()
    if not token:
        await message.reply("❗ Please specify the token you want to report. Example: /report FAKE")
        return
    await message.reply(f"⚠️ Token `{token}` has been flagged for review. Our team will investigate it.")

if __name__ == '__main__':
    executor.start_polling(dp)
