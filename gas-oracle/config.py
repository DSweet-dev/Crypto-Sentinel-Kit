import os
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

# Налаштовуємо пороги для рекомендацій (в Gwei)
GAS_LOW_THRESHOLD = 20
GAS_HIGH_THRESHOLD = 50
