# Trading Bot – Binance Futures Testnet

## Overview

This project is a simplified Trading Bot built using Python that interacts with the Binance Futures Testnet API. The application allows users to place MARKET and LIMIT orders through a Command Line Interface (CLI).

The main objective of this project is to demonstrate:

* API integration
* CLI argument handling
* Input validation
* Logging
* Exception handling
* Clean and reusable project structure

This project was developed as part of a Python Developer Internship Assignment.

---

# Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL order types
* Binance Futures Testnet integration
* Command Line Interface using argparse
* Input validation
* Logging for API responses and errors
* Exception handling for invalid inputs and API failures

---

# Technologies Used

* Python 3.x
* python-binance
* argparse
* logging

---

# Project Structure

```text
Trading_Bot/
│
├── cli.py
├── client.py
├── orders.py
├── validators.py
├── logging_config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── logs/
│   └── trading_bot.log
```

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <your_repository_link>
cd Trading_Bot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
.\venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Binance Futures Testnet Setup

1. Create a Binance Futures Testnet account.
2. Generate API Key and Secret Key.
3. Add your API credentials inside `client.py`.

Testnet URL used:

```python
https://testnet.binancefuture.com/fapi
```

---

# How to Run

## MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000
```

---

# Example Output

```text
Order placed successfully

{
    'orderId': 123456,
    'symbol': 'BTCUSDT',
    'status': 'NEW',
    'side': 'BUY',
    'type': 'MARKET'
}
```

---

# Logging

All API requests, responses, and errors are stored inside:

```text
logs/trading_bot.log
```

Example log:

```text
2026-06-03 11:56:32,860 - INFO - Order Success
```

---

# Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Missing LIMIT order price
* Binance API errors
* Network related exceptions

---

# Future Improvements

* Add Stop-Limit orders
* Add interactive CLI menus
* Add lightweight dashboard/UI
* Add unit testing
* Add order history tracking

---

# Author

Venkat Sai Charan Saragani
