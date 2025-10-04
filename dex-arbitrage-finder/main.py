import time
from web3 import Web3
import config

w3 = Web3(Web3.HTTPProvider(config.NODE_HTTP_URL))

# Ініціалізуємо контракти роутерів
uniswap_router = w3.eth.contract(address=config.UNISWAP_V2_ROUTER, abi=config.ROUTER_ABI)
sushiswap_router = w3.eth.contract(address=config.SUSHISWAP_ROUTER, abi=config.ROUTER_ABI)

def get_price(router, amount_in_wei, path):
    """Отримує ціну обміну через роутер DEX."""
    try:
        amounts_out = router.functions.getAmountsOut(amount_in_wei, path).call()
        return amounts_out[1]  # Повертаємо кількість токена, який отримуємо
    except Exception as e:
        print(f"Error getting price: {e}")
        return 0

def check_arbitrage():
    """Перевіряє можливість арбітражу."""
    print("Checking prices...")
    
    amount_in = 1  # Кількість WETH для перевірки
    amount_in_wei = w3.to_wei(amount_in, 'ether')
    
    # Шлях обміну: WETH -> USDC
    trade_path = [config.WETH_ADDRESS, config.USDC_ADDRESS]

    # Отримуємо ціни
    # 1 WETH -> ? USDC на Uniswap
    uniswap_price = get_price(uniswap_router, amount_in_wei, trade_path)
    # 1 WETH -> ? USDC на Sushiswap
    sushiswap_price = get_price(sushiswap_router, amount_in_wei, trade_path)
    
    # Конвертуємо результат з 6 десяткових знаків (специфіка USDC)
    uniswap_usdc = uniswap_price / 10**6
    sushiswap_usdc = sushiswap_price / 10**6
    
    print(f"Uniswap price for 1 WETH: {uniswap_usdc:.2f} USDC")
    print(f"Sushiswap price for 1 WETH: {sushiswap_usdc:.2f} USDC")
    
    # Порівнюємо ціни та розраховуємо різницю
    price_diff = abs(uniswap_usdc - sushiswap_usdc)
    profit_percentage = (price_diff / max(uniswap_usdc, sushiswap_usdc)) * 100 if max(uniswap_usdc, sushiswap_usdc) > 0 else 0
    
    if profit_percentage > 0.5: # Шукаємо різницю більше 0.5%
        print(f"\n🚨 Arbitrage Opportunity Found! 🚨")
        print(f"   Difference: {price_diff:.2f} USDC ({profit_percentage:.2f}%)")
    else:
        print("No significant arbitrage opportunity found.")
    print("-" * 30)

if __name__ == "__main__":
    while True:
        check_arbitrage()
        time.sleep(60) # Перевіряємо кожну хвилину
