from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from src.clients.llm_client import llm_client
from src.config.prompts import prompt_text_extraction


# Create the prompt template for text extraction.
text_extraction_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", prompt_text_extraction.prompt),
        ("human", "Text: {text}\nQuery: {query}"),
    ]
)

# Create the chain for text extraction.
text_extraction_chain = text_extraction_prompt | llm_client | StrOutputParser()
