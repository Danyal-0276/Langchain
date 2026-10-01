from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOllama(model="qwen2.5:3b")


class Review(TypedDict):
    key_themes: Annotated[list[str], "List of key themes discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[
        Literal["positive", "negative", "neutral"],
        "Return sentiment of the review, either 'positive', 'negative', or 'neutral'",
    ]
    pros: Annotated[Optional[list[str]], "List of pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "List of cons mentioned in the review"]
    name: Annotated[Optional[str], "Name of the reviewer, if available"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """the hardware is great but software feels bloated and slow, there are too many pre-installed apps that I don't need, and the battery life is disappointing. Overall, I'm not satisfied with this product."""
)

print(type(result))  # Output: <class 'dict'>
print(result)  # Output: {'summary': 'The hardware is good, but the software is bloated and slow with unnecessary pre-installed apps. The battery life is disappointing, leading to overall dissatisfaction with the product.', 'sentiment': 'negative', 'name': None}
print(
    result["summary"]
)  # Output: The hardware is good, but the software is bloated and slow with unnecessary pre-installed apps. The battery life is disappointing, leading to overall dissatisfaction with the product.
print(result["sentiment"])  # Output: negative
print(result["name"])  # Output: None


