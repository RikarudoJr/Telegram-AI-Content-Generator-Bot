from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)
from openai_service import generate_prompt_response

# State definitions for simple start flow
STEP_1, STEP_2 = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and resets user session state."""
    # Clear any previous session data (Reset State)
    context.user_data.clear()

    await update.message.reply_text(
        "🚀 Welcome aboard! Let's generate a post together.\n\n"
        "Let's create a custom post together.\n"
        "**Step 1/2**: What topic would you like to write about?"
    )
    return STEP_1

async def collect_step1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Collects input for Step 1 and acknowledges it."""
    user_input = update.message.text.strip()
    context.user_data["topic"] = user_input


    await update.message.reply_text(
        f"Received: '{user_input}'!\n"
        "**Step 2/2**: What tone do you want to use?"
    )
    return STEP_2

async def collect_step2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Collects tone, calls OpenAI asynchronously, returns response, and resets state."""
    user_tone = update.message.text.strip()
    context.user_data["tone"] = user_tone

    topic = context.user_data.get("topic", "N/A")

    await update.message.reply_text("⏳ Processing your request with OpenAI... Please wait!")

    # Call OpenAI API asynchronously
    ai_response = await generate_prompt_response(topic=topic, tone=user_tone)

    await update.message.reply_text(
        f"✨ **Here is your generated post:**\n\n{ai_response}\n\n"
        "Send /start to create another post!"
    )

    # Clear user session data and end conversation state
    context.user_data.clear()
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and resets the conversation state."""
    context.user_data.clear()
    await update.message.reply_text(
        "❌ Conversation canceled and state reset. Send /start whenever you want to try again!"
    )
    return ConversationHandler.END

async def reset(update:Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.clear()
    await update.message.reply_text(
        "session reset clean!"
    )
    return ConversationHandler.END

def get_conversation_handler() -> ConversationHandler:
    """Returns the simplified ConversationHandler for start & reset flow."""
    return ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            STEP_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_step1)],
            STEP_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, collect_step2)]
        },
        fallbacks=[CommandHandler("cancel", cancel), CommandHandler("reset",reset)],
    )

