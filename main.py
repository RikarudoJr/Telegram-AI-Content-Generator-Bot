import logging
# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)
from telegram.ext import ApplicationBuilder
import config
from bot_handlers import get_conversation_handler



def main():
    if not config.TELEGRAM_BOT_TOKEN or config.TELEGRAM_BOT_TOKEN == "your_telegram_bot_token_here":
        logger.error("Error: TELEGRAM_BOT_TOKEN is missing or not set in .env")
        return

    # Build the Application
    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    # Add conversation handler
    conv_handler = get_conversation_handler()
    app.add_handler(conv_handler)

    logger.info("Bot is starting polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
