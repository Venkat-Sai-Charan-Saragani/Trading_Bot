# Import logging module
import logging
# Import os module to create folders
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logging settings
logging.basicConfig(
    filename="logs/trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Logging started")