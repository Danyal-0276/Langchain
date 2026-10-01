from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
model = ChatOllama(model="qwen2.5:3b")

chat_history = [SystemMessage(content="You are a helpful assistant")]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print("chat history: ", chat_history)
