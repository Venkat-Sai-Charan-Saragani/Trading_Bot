# Import client function
from client import get_client

# Import logging module
import logging

# Get Binance client object
client = get_client()

# Function to place orders
def place_order(symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }


    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"


    try:
        # Send order request to Binance
        response = client.futures_create_order(**params)

        # Save successful order in log file
        logging.info(f"Order Sucess: {response}")

        return response

    except Exception as e:
        # Save error in log file
        logging.error(f"Order Failed: {str(e)}")
        raise
