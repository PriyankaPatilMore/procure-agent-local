from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from tools import get_supplier_metrics, search_contract

llm = ChatOllama(model="llama3.2", temperature=0)
tools = [get_supplier_metrics, search_contract]
agent_executor = create_react_agent(llm, tools)

def chat(prompt):
    print(f"\nQuery: {prompt}")
    print("-" * 40)
    response = agent_executor.invoke({"messages": [("user", prompt)]})
    print(f"Agent: {response['messages'][-1].content}")

if __name__ == "__main__":
    chat("What is the risk level for GlobalTech Solutions?")
