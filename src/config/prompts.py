from pydantic import BaseModel, Field


class PreConfigPrompt(BaseModel):
    """A prompt to configure the agent before starting the main task.

    Attributes:
        prompt: The prompt to configure the agent.
    """

    prompt: str = Field(
        ...,
        description="The prompt to configure the agent before starting the main task.",
    )


prompt_text_extraction = PreConfigPrompt(
    prompt=(
        "You are a helpful assistant that extracts text from texts. You'll be "
        "given a text and a query to extract from the text. Return all "
        "possible matches with a very short explanation. If the text does not "
        "contain any matches, return 'No matches found'."
    )
)
