from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from src.config.model_config import gemini_flash, openai_gpt5


# Initialize different LLM clients based on configurations.
llm_client_gemini = ChatGoogleGenerativeAI(
    model=gemini_flash.model_name,
    base_url=gemini_flash.base_url,
    temperature=gemini_flash.temperature,
    max_output_tokens=gemini_flash.max_output_tokens,
)

llm_client_openai = ChatOpenAI(
    model=openai_gpt5.model_name,
    temperature=openai_gpt5.temperature,
    max_tokens=openai_gpt5.max_output_tokens,
)

# Select the LLM client to use here.
llm_client = llm_client_openai
