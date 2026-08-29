from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

texts = [
    "Islamabad is the capital of pakistan.",
    "The largest city in pakistan is karachi.",
    "The smallest province in pakistan is balochistan.",
]
vector=embedding.embed_documents(texts)

print(str(vector))

