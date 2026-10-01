from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# chat template

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a {domain} expert"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "Explain in simple Terms, what is {topic}"),
    ]
)

chat_history = []
# load chat history
with open("chat_history.json", "r") as f:
    chat_history = f.read()
# create prompt
prompt = chat_template.invoke(
    {"domain": "cricket", "topic": "offside", "chat_history": chat_history}
)
print(prompt)  # List of messages with filled-in content
