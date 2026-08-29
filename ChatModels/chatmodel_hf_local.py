from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 128,
        "temperature": 0.7,
    }
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Pakistan?")

print(result.content)