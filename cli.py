# Import argparse for command line arguments
import argparse

# Import logging configuration
import logging_config

# Import order placement function
from orders import place_order

# Import validation functions
from validators import validate_side, validate_order_type

# Create argument parser object
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

# Store user input arguments
args = parser.parse_args()

try:
    validate_side(args.side)
    validate_order_type(args.type)

    if args.type == "LIMIT" and not args.price:
        raise ValueError("Price required for LIMIT order")

    response = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\nOrder placed successfully")
    print(response)

except Exception as e:
    print(f"Error: {e}")
