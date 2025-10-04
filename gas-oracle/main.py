import time
import requests
import config

def get_gas_prices():
    """Отримує ціни на газ з API Etherscan."""
    url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={config.ETHERSCAN_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["status"] == "1":
            return {
                "safe": int(data["result"]["SafeGasPrice"]),
                "propose": int(data["result"]["ProposeGasPrice"]),
                "fast": int(data["result"]["FastGasPrice"])
            }
        else:
            print(f"API Error: {data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None

def get_recommendation(gas_price):
    """Надає рекомендацію на основі ціни на газ."""
    if gas_price < config.GAS_LOW_THRESHOLD:
        return "✅ Excellent time to transact! Gas is very low."
    elif config.GAS_LOW_THRESHOLD <= gas_price < config.GAS_HIGH_THRESHOLD:
        return "👍 Normal gas price. Good for regular transactions."
    else:
        return "🔥 High gas price! Consider waiting if your transaction is not urgent."

def display_gas_info():
    """Відображає інформацію про газ."""
    prices = get_gas_prices()
    if prices:
        print("--- Ethereum Gas Oracle ---")
        print(f"🐢 Safe (Slow):   {prices['safe']} Gwei")
        print(f"🚶 Propose (Avg): {prices['propose']} Gwei")
        print(f"🚀 Fast (Fast):    {prices['fast']} Gwei")
        print("-" * 27)
        recommendation = get_recommendation(prices['propose'])
        print(f"Recommendation: {recommendation}")
        print("-" * 27)

if __name__ == "__main__":
    while True:
        display_gas_info()
        print("Updating in 60 seconds...")
        time.sleep(60)
