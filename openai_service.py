import logging
from openai import AsyncOpenAI
import config

logger = logging.getLogger(__name__)

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=config.OPENAI_API_KEY,
)

async def generate_prompt_response(topic: str, tone: str) -> str:
    """
    Sends the user's topic and tone to OpenRouter API and returns the generated content.
    Uses async client to prevent blocking the telegram bot event loop.
    """
    system_prompt = (
        "You are a helpful content creator assistant. "
        "Create a short piece of writing based on the user's requested topic and tone."
    )
    user_prompt = f"Topic: {topic}\nTone: {tone}"

    try:
        response = await client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=300,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Error calling OpenRouter API: {e}")
        return "Sorry, I encountered an error generating your response with OpenRouter. Please check your API key and try again."
