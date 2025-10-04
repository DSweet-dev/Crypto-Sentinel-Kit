import time
import requests
import config

# Словник для зберігання хешів останніх оброблених транзакцій
last_tx_hashes = {wallet["address"]: None for wallet in config.WALLETS_TO_TRACK}

def send_telegram_message(message):
    """Надсилає повідомлення в Telegram."""
    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": config.TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Telegram notification sent!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Telegram message: {e}")

def check_wallet_transactions(wallet):
    """Перевіряє транзакції для одного гаманця."""
    address = wallet["address"]
    url = (f"https://api.etherscan.io/api?module=account&action=txlist&address={address}"
           f"&startblock=0&endblock=99999999&sort=desc&page=1&offset=5"
           f"&apikey={config.ETHERSCAN_API_KEY}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["status"] == "1" and data["result"]:
            latest_tx = data["result"][0]
            tx_hash = latest_tx["hash"]
            
            # Якщо це нова транзакція, обробляємо її
            if last_tx_hashes[address] != tx_hash:
                last_tx_hashes[address] = tx_hash # Оновлюємо хеш
                
                # Не надсилати сповіщення при першому запуску
                if last_tx_hashes[address] is None:
                     last_tx_hashes[address] = tx_hash
                     print(f"Initial transaction for {wallet['name']} set to {tx_hash[:10]}...")
                     return

                value_eth = int(latest_tx['value']) / 10**18
                direction = "➡️ Incoming" if latest_tx['to'].lower() == address.lower() else "⬅️ Outgoing"
                
                message = (
                    f"🔔 *New Transaction for {wallet['name']}* 🔔\n\n"
                    f"{direction}\n"
                    f"*Value:* {value_eth:.4f} ETH\n"
                    f"*From:* `{latest_tx['from']}`\n"
                    f"*To:* `{latest_tx['to']}`\n\n"
                    f"[View on Etherscan](https://etherscan.io/tx/{tx_hash})"
                )
                send_telegram_message(message)
                
    except Exception as e:
        print(f"Error checking wallet {wallet['name']}: {e}")

if __name__ == "__main__":
    print("Starting wallet tracker...")
    while True:
        for wallet_info in config.WALLETS_TO_TRACK:
            check_wallet_transactions(wallet_info)
            time.sleep(5) # Невелика затримка між запитами до API
        print("Cycle finished. Waiting for 30 seconds...")
        time.sleep(30)
