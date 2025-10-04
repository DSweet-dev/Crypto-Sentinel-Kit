import time
import requests
import config

def get_nft_floor_price(collection_slug):
    """Отримує floor price для NFT-колекції з OpenSea API."""
    url = f"https://api.opensea.io/api/v2/collections/{collection_slug}/stats"
    headers = {
        "accept": "application/json",
        "X-API-KEY": config.OPENSEA_API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        floor_price = data.get("total", {}).get("floor_price")
        if floor_price is not None:
            # OpenSea API v2 повертає ціну в найменших одиницях (Wei)
            return floor_price / (10**18)
        else:
            print(f"Could not find floor price for {collection_slug} in the response.")
            return None
            
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error for {collection_slug}: {e.response.status_code} - {e.response.text}")
        return None
    except Exception as e:
        print(f"An error occurred for {collection_slug}: {e}")
        return None

def display_floor_prices():
    """Відображає floor price для всіх відстежуваних колекцій."""
    print("--- NFT Floor Price Tracker (OpenSea) ---")
    for slug in config.COLLECTIONS_TO_TRACK:
        price = get_nft_floor_price(slug)
        if price is not None:
            print(f"  - {slug.capitalize()}: {price:.3f} ETH")
        else:
            print(f"  - {slug.capitalize()}: Failed to fetch price")
        time.sleep(1) # Затримка, щоб не перевищити ліміт API
    print("-" * 41)

if __name__ == "__main__":
    if not config.OPENSEA_API_KEY:
        print("Error: OpenSea API key not found. Please set OPENSEA_API_KEY in your .env file.")
    else:
        while True:
            display_floor_prices()
            print("Updating in 5 minutes...")
            time.sleep(300)
