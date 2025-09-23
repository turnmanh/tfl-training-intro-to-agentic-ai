from langchain_google_genai import ChatGoogleGenerativeAI

from src.config.model_config import gemini_flash


llm_client = ChatGoogleGenerativeAI(
    model=gemini_flash.model_name,
    temperature=gemini_flash.temperature,
    max_output_tokens=gemini_flash.max_output_tokens,
)