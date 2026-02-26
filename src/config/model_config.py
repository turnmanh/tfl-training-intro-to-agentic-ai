import os 

from pydantic import BaseModel, Field
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from a .env file.


class ModelConfig(BaseModel):
    model_name: str = Field(..., description="The name of the model to be used.")
    api_key: str = Field(..., description="The API key for accessing the model service.")
    temperature: float = Field(default=0.7, description="Sampling temperature for the model.")


class GeminiModelConfig(ModelConfig):
    """Configuration specific to Gemini models."""
    model_name: str = "gemini-2.5-flash" 
    max_output_tokens: int = Field(default=1024, description="Maximum number of output tokens.")


class OpenAIModelConfig(ModelConfig):
    """Configuration specific to OpenAI models."""
    model_name: str = "gpt-5" 
    max_output_tokens: int = Field(default=2048, description="Maximum number of output tokens.")


gemini_flash = GeminiModelConfig(
    api_key=os.getenv("GOOGLE_API_KEY", ""),
    temperature=0.7,
)


openai_gpt41_nano = OpenAIModelConfig(
    model_name="gpt-4.1-nano",
    api_key=os.getenv("OPENAI_API_KEY", ""),
    temperature=0.7,
    max_output_tokens=2048,
)


openai_gpt4o_mini = OpenAIModelConfig(
    model_name="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY", ""),
    temperature=0.7,
    max_output_tokens=2048 * 2,
)


openai_gpt5 = OpenAIModelConfig(
    api_key=os.getenv("OPENAI_API_KEY", ""),
    temperature=0.7,
    max_output_tokens=2048 * 4,
)
