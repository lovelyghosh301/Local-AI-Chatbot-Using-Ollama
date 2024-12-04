
from langchain_ollama import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate as cpt
ol=OllamaLLM(model="llama3")
#result=ol.invoke(input="in what context is the term hello world generally used in?")
#print(result)
template="""
Answer the Questions below.
Here is the conversation history: {context}
Question: {question}
Answer:
"""
prompt=  cpt.from_template(template)
chain=prompt | ol
#op=chain.invoke({"context":"","question":"What is lang chain? explain in 2 sentences"})
#hiprint(op)
def handle_conversations():
    context=""
    print("Welcome to the AI ChatBot! Type '/die' to quit.")
    while True:
        user_input=input("You: ")
        if user_input.lower()=="/die":
            break
        res=chain.invoke({"context":context,"question":user_input})
        print("Bot: ",res)
        context+=f"\nUser: {user_input}\nAI:{res}"

if __name__=="__main__":
    handle_conversations()