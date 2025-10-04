#  Crypto-Sentinel-Kit 🛡️

<div align="center">
  <img src="https://path.to/your/simple/logo.png" alt="Project Logo" width="150"/>
</div>

<p align="center">
  <strong>A versatile Python toolkit for monitoring on-chain events, analyzing DeFi protocols, and automating crypto tasks. Your personal sentinel for the blockchain world.</strong>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" alt="Python Version">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
    <img src="https://img.shields.io/github/stars/DSweet-dev/Crypto-Sentinel-Kit?style=social" alt="GitHub Stars">
</p>

---

## 🌟 About The Project

**Crypto-Sentinel-Kit** is a collection of powerful, standalone Python scripts designed for developers, traders, and crypto enthusiasts. Instead of relying on monolithic applications, this toolkit provides focused, easy-to-use scripts to get specific on-chain information quickly and efficiently.

Whether you want to hunt for whale transactions, find arbitrage opportunities, or simply check the floor price of your favorite NFT collection, this kit has a tool for you.

---

## ✨ Key Features

* **🔍 Real-time Mempool Scanner**: Detect whale-sized transactions in the Ethereum mempool before they are confirmed.
* **⚖️ DEX Arbitrage Finder**: Spot price differences for token pairs on Uniswap and Sushiswap.
* **🔔 Telegram Wallet Tracker**: Get instant Telegram notifications for new transactions on any Ethereum wallet.
* **⛽ Gas Oracle**: Fetch current gas prices (Slow, Average, Fast) and get a simple recommendation.
* **🖼️ NFT Floor Pricer**: Check the latest floor price for any NFT collection on OpenSea.

---

## 🛠️ Tech Stack

This project is built with Python and utilizes the following core libraries:

* **Web3.py**: For interacting with the Ethereum blockchain.
* **Requests**: For making API calls to services like Etherscan and OpenSea.
* **Asyncio/Websockets**: For real-time data streaming from blockchain nodes.
* **Python-dotenv**: For managing environment variables and API keys securely.

---

## 🚀 Getting Started

Follow these steps to get the toolkit up and running on your local machine.

### Prerequisites

* Python 3.9 or higher
* Git
* An Ethereum Node URL (e.g., from [Alchemy](https://www.alchemy.com/) or [Infura](https://www.infura.io/)) for the Mempool Scanner and Arbitrage Finder.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YourUsername/Crypto-Sentinel-Kit.git](https://github.com/YourUsername/Crypto-Sentinel-Kit.git)
    cd Crypto-Sentinel-Kit
    ```

2.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    * Create a copy of the example `.env` file:
        ```sh
        cp .env.example .env
        ```
    * Open the `.env` file and add your own API keys and node URLs.
        ```ini
        # .env file
        NODE_WSS_URL="wss://mainnet.infura.io/ws/v3/YOUR_INFURA_KEY"
        NODE_HTTP_URL="[https://mainnet.infura.io/v3/YOUR_INFURA_KEY](https://mainnet.infura.io/v3/YOUR_INFURA_KEY)"
        ETHERSCAN_API_KEY="YOUR_ETHERSCAN_API_KEY"
        OPENSEA_API_KEY="YOUR_OPENSEA_API_KEY"
        TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
        TELEGRAM_CHAT_ID="YOUR_TELEGRAM_CHAT_ID"
        ```

---

## 📖 Usage

Each script can be run independently from the root directory.

### 1. Mempool Scanner

Monitors the Ethereum mempool for transactions exceeding a defined ETH value.

**Run the script:**
```sh
python mempool-scanner/main.py
```

**Example Output:**
```
Subscribed to new pending transactions...
-----------------------------------------
🐋 WHALE ALERT! 🐋
  From: 0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B
  To: 0x73BCEb1Cd57C711feC4224D8125b931Cc7341363
  Value: 150.00 ETH
  Hash: 0x1a2b3c...
-----------------------------------------
```

### 2. DEX Arbitrage Finder

Checks for price discrepancies between Uniswap and Sushiswap for the WETH/USDC pair.

**Run the script:**
```sh
python dex-arbitrage-finder/main.py
```

**Example Output:**
```
Checking prices...
Uniswap price for 1 WETH: 3005.50 USDC
Sushiswap price for 1 WETH: 3020.75 USDC

🚨 Arbitrage Opportunity Found! 🚨
   Difference: 15.25 USDC (0.50%)
------------------------------
```

### 3. Wallet Tracker

Sends a Telegram notification when a new transaction is detected for a monitored wallet.

**Run the script:**
```sh
python wallet-tracker/main.py
```

**Example Output (in your terminal):**
```
Starting wallet tracker...
Telegram notification sent!
Cycle finished. Waiting for 30 seconds...
```

### 4. Gas Oracle

Fetches current gas prices and provides a recommendation.

**Run the script:**
```sh
python gas-oracle/main.py
```

**Example Output:**
```
--- Ethereum Gas Oracle ---
🐢 Safe (Slow):   15 Gwei
🚶 Propose (Avg): 18 Gwei
🚀 Fast (Fast):    22 Gwei
---------------------------
Recommendation: ✅ Excellent time to transact! Gas is very low.
---------------------------
```

### 5. NFT Floor Pricer

Retrieves the floor price for pre-defined NFT collections from OpenSea.

**Run the script:**
```sh
python nft-floor-pricer/main.py
```

**Example Output:**
```
--- NFT Floor Price Tracker (OpenSea) ---
  - Boredapeyachtclub: 25.500 ETH
  - Cryptopunks: 28.150 ETH
  - Azuki: 4.890 ETH
---------------------------------------
```

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 📬 Contact

[Twitter](https://x.com/McSladkyi) - dsoolodbkiyb10@gmail.com

Project Link: [https://github.com/DSweet-dev/Crypto-Sentinel-Kit](https://github.com/DSweet-dev/Crypto-Sentinel-Kit)
