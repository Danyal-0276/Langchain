# Changed: Import ChatHuggingFace and HuggingFacePipeline instead of ChatOllama
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, EmailStr, Field

# Added: Required for loading the Hugging Face pipeline
from transformers import pipeline

load_dotenv()

# Changed: Replaced ChatOllama with a local Hugging Face pipeline
# 1. Load the TinyLlama model locally using the transformers pipeline
local_llm = pipeline(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={"torch_dtype": "auto", "device_map": "auto"}
)

# 2. Wrap the local pipeline in LangChain's HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=local_llm)

# 3. Create the ChatHuggingFace model instance
model = ChatHuggingFace(llm=llm)


class Review(BaseModel):
    key_themes: list[str] = Field(
        description="List of key themes discussed in the review"
    )
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Return sentiment of the review, either 'positive', 'negative', or 'neutral'"
    )

    pros: Optional[list[str]] = Field(
        description="List of pros mentioned in the review"
    )
    cons: Optional[list[str]] = Field(
        description="List of cons mentioned in the review"
    )
    name: Optional[str] = Field(description="Name of the reviewer, if available")


# Note: Ensure your langchain-huggingface version supports Pydantic structured output
# https://github.com/langchain-ai/langchain/pull/34708
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """the hardware is great but software feels bloated and slow, there are too many pre-installed apps that I don't need, and the battery life is disappointing. Overall, I'm not satisfied with this product."""
)

print(result.name)  # Output: None
print(result.summary)  # Output: The hardware is great but software feels bloated and slow, there are too many pre-installed apps that I don't need, and the battery life is disappointing. Overall, I'm not satisfied with this product.
print(result.sentiment)  # Output: negative
print(result.pros)  # Output: None
print(result.cons)  # Output: ['software feels bloated and slow', 'too many pre-installed apps', 'battery life is disappointing']
print(result.key_themes)  # Output: ['hardware', 'software', 'pre-installed apps', 'battery life']
print(result.dict())  # Output: {'key_themes': ['hardware', 'software', 'pre-installed apps', 'battery life'], 'summary': "The hardware is great but software feels bloated and slow, there are too many pre-installed apps that I don't need, and the battery life is disappointing. Overall, I'm not satisfied with this product.", 'sentiment': 'negative', 'pros': None, 'cons': ['software feels bloated and slow', 'too many pre-installed apps', 'battery life is disappointing'], 'name': None}
print(result.model_dump_json())  # Output: {"key_themes": ["hardware", "software", "pre-installed apps", "battery life"], "summary": "The hardware is great but software feels bloated and slow, there are too many pre-installed apps that I don't need, and the battery life is disappointing. Overall, I'm not satisfied with this product.", "sentiment": "negative", "pros": null, "cons": ["software feels bloated and slow", "too many pre-installed apps", "battery life is disappointing"], "name": null}
print(result)