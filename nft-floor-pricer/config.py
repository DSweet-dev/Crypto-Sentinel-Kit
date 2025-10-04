import os
from dotenv import load_dotenv

load_dotenv()

# Отримайте ключ на https://docs.opensea.io/reference/request-an-api-key
OPENSEA_API_KEY = os.getenv("OPENSEA_API_KEY")

# Slugs (короткі назви) колекцій для відстеження
COLLECTIONS_TO_TRACK = [
    "boredapeyachtclub",
    "cryptopunks",
    "azuki"
]
