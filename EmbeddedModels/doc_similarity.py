from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Islamabad is the capital of Pakistan.",
    "The largest city in Pakistan is Karachi.",
    "The smallest province in Pakistan is Balochistan.",
    "Pakistan is a country in South Asia.",
    "The official language of Pakistan is Urdu.",
]

query = "Tell me about thePakistan?"

# Generate embeddings
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Compare the query with every document
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

print("Query:", query)
print("Cosine Similarity Scores:")
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
print(documents[index], score)