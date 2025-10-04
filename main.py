import asyncio
from web3 import Web3
import config

# Конвертуємо поріг з ETH в Wei для порівняння
WHALE_THRESHOLD_WEI = Web3.to_wei(config.WHALE_THRESHOLD_ETH, 'ether')

def handle_transaction(tx):
    """Обробляє транзакцію і перевіряє, чи є вона "китовою"."""
    try:
        # Перевіряємо, чи є ключ 'value' і чи сума перевищує поріг
        if 'value' in tx and tx['value'] > WHALE_THRESHOLD_WEI:
            value_in_eth = Web3.from_wei(tx['value'], 'ether')
            print("-----------------------------------------")
            print(f"🐋 WHALE ALERT! 🐋")
            print(f"  From: {tx['from']}")
            print(f"  To: {tx['to']}")
            print(f"  Value: {value_in_eth:.2f} ETH")
            print(f"  Hash: {tx['hash'].hex()}")
            print("-----------------------------------------")
    except Exception as e:
        print(f"Error processing transaction: {e}")

async def subscribe_to_pending_transactions(web3_instance):
    """Підписується на потік нових pending-транзакцій."""
    subscription_id = await web3_instance.eth.subscribe('newPendingTransactions')
    print("Subscribed to new pending transactions...")
    
    # Асинхронно слухаємо потік
    async for tx_hash in subscription_id:
        try:
            tx = await web3_instance.eth.get_transaction(tx_hash)
            if tx:
                handle_transaction(tx)
        except Exception as e:
            # Іноді транзакція зникає з мемпулу, це нормально
            # print(f"Could not get tx details for hash {tx_hash.hex()}: {e}")
            pass

async def main():
    # Підключаємось до ноди через WebSocket
    w3 = Web3(Web3.WebsocketProvider(config.NODE_WSS_URL))
    print(f"Connected to Ethereum node: {await w3.is_connected()}")
    
    # Запускаємо слухача
    await subscribe_to_pending_transactions(w3)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScanner stopped by user.")
