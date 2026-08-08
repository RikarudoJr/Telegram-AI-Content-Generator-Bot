import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN == "your_telegram_bot_token_here":
    logger.warning("TELEGRAM_BOT_TOKEN is not set properly in .env")

if not OPENAI_API_KEY or OPENAI_API_KEY == "your_openai_api_key_here":
    logger.warning("OPENAI_API_KEY is not set properly in .env")
