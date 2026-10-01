from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, EmailStr, Field

load_dotenv()

model = ChatOllama(model="qwen2.5:3b")

json_schema = {
    "title": "Product Review Analysis",
    "description": "A schema for analyzing product reviews, extracting key themes, summarizing the review, determining sentiment, and identifying pros and cons.",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "A list of key themes or topics mentioned in the review.",
        },
        "summary": {
            "type": "string",
            "description": "A concise summary of the review.",
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "The overall sentiment of the review.",
        },
        "pros": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "A list of positive aspects mentioned in the review, if any.",
        },
        "cons": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "A list of negative aspects mentioned in the review, if any.",
        },
        "name": {
            "type": ["string", "null"],
            "description": "(Optional) The name of the reviewer, if available.",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}


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


structured_model = model.with_structured_output(json_schema=json_schema)

result = structured_model.invoke(
    """the hardware is great but software feels bloated and slow, there are too many pre-installed apps that I don't need, and the battery life is disappointing. Overall, I'm not satisfied with this product."""
)

print(result.name)  # Output: None
print(
    result.summary
)  # Output: The hardware is great but software feels bloated and slow, there are too many pre-installed apps that I don't need, and the battery life is disappointing. Overall, I'm not satisfied with this product.
print(result.sentiment)  # Output: negative
print(result.pros)  # Output: None
print(
    result.cons
)  # Output: ['software feels bloated and slow', 'too many pre-installed apps', 'battery life is disappointing']
print(
    result.key_themes
)  # Output: ['hardware', 'software', 'pre-installed apps', 'battery life']
print(
    result.dict()
)  # Output: {'key_themes': ['hardware', 'software', 'pre-installed apps', 'battery life'], 'summary': "The hardware is great but software feels bloated and slow, there are too many pre-installed apps that I don't need, and the battery life is disappointing. Overall, I'm not satisfied with this product.", 'sentiment': 'negative', 'pros': None, 'cons': ['software feels bloated and slow', 'too many pre-installed apps', 'battery life is disappointing'], 'name': None}
print(
    result.model_dump_json()
)  # Output: {"key_themes": ["hardware", "software", "pre-installed apps", "battery life"], "summary": "The hardware is great but software feels bloated and slow, there are too many pre-installed apps that I don't need, and the battery life is disappointing. Overall, I'm not satisfied with this product.", "sentiment": "negative", "pros": null, "cons": ["software feels bloated and slow", "too many pre-installed apps", "battery life is disappointing"], "name": null}
print(result)
