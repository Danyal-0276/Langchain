from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model="qwen2.5:3b")

chat_template = ChatPromptTemplate(
    [
        ('system','You are a {domain} expert'),
        
        ('human','Explain in simple Terms, what is {topic}'),
    ]
)

prompt = chat_template.invoke({"domain": "cricket", "topic": "offside"})


print(prompt)  # List of messages with filled-in content
