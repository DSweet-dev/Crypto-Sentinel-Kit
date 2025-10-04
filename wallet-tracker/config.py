import os
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Гаманці для відстеження
WALLETS_TO_TRACK = [
    {"name": "Vitalik Buterin", "address": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"},
    {"name": "Example Wallet 2", "address": "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"},
]
