from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

model = ChatOllama(model="qwen2.5:3b")
 
messages = [SystemMessage(content="You are a helpful assistant"),
            HumanMessage(content="tell me a joke"),]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)