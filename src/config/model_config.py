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


gemini_flash = GeminiModelConfig(
    api_key=os.getenv("GOOGLE_API_KEY", ""),
    temperature=0.7,
)
