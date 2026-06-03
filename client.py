# Import Binance Client class
from binance.client import Client

# to load the api credietntials in env
from dotenv import load_dotenv
import os

load_dotenv()


# API credentials
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")


# Create Binance client object
client = Client(api_key, api_secret)


# Connect to Binance Futures Testnet
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'


# Function to return client object
def get_client():
    return client


