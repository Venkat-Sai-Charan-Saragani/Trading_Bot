# Function to validate BUY or SELL input
def validate_side(side):
    # Check if side is valid
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


# Function to validate order type
def validate_order_type(order_type):
    # Check if order type is valid
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
