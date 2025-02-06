import os
from dotenv import load_dotenv

load_dotenv()

TG_BOT_TOKEN = os.getenv("BOT_TOKEN")
CALORIENINJAS = os.getenv("CALORIENINJAS")
OPENWEATHER_TOKEN = os.getenv("OPENWEATHER_TOKEN")
RAPID_TOKEN = os.getenv("RAPID_TOKEN")

if not TG_BOT_TOKEN:
    raise ValueError("Не указан токен телеграм-бота в переменной окружения BOT_TOKEN!")
