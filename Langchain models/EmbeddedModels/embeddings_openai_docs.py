from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=36)

document = [
    "Islamabad is the capital of pakistan.",
    "The largest city in pakistan is karachi.",
    "The smallest province in pakistan is balochistan.",
    "Pakistan is a country in south asia."
]

result = embedding.embed_documents(document)
print(str(result))
