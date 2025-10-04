import os
from dotenv import load_dotenv

load_dotenv()

# Вставте ваш WebSocket URL від Alchemy або Infura
NODE_WSS_URL = os.getenv("NODE_WSS_URL", "wss://mainnet.infura.io/ws/v3/your-infura-key")

# Поріг для "кита" в ETH. Наприклад, 100 ETH.
WHALE_THRESHOLD_ETH = 100
