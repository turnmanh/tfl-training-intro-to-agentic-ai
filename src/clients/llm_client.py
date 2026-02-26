from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from src.config.model_config import (
    OpenAIModelConfig, 
    gemini_flash, 
    openai_gpt41_nano,
    openai_gpt4o_mini, 
    openai_gpt5
)

openai_model: OpenAIModelConfig = openai_gpt41_nano

# Initialize different LLM clients based on configurations.
llm_client_gemini = ChatGoogleGenerativeAI(
    model=gemini_flash.model_name,
    temperature=gemini_flash.temperature,
    max_output_tokens=gemini_flash.max_output_tokens,
)

llm_client_openai = ChatOpenAI(
    model=openai_model.model_name,
    temperature=openai_model.temperature,
    max_tokens=openai_model.max_output_tokens,  # type: ignore
)

# Select the LLM client to use here.
llm_client = llm_client_openai
