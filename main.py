import os
from dotenv import load_dotenv

load_dotenv()

from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from tools import get_supplier_metrics, search_contract

llm = ChatOllama(model="llama3.2", temperature=0)
tools = [get_supplier_metrics, search_contract]

system_message = "You are a procurement AI. Use the provided tools to answer questions. If you don't know, say you don't know."
agent_executor = create_react_agent(llm, tools, state_modifier=system_message)


def chat(prompt):
    print(f"\nQuery: {prompt}")
    print("-" * 40)
    response = agent_executor.invoke({"messages": [("user", prompt)]})
    print(f"Agent: {response['messages'][-1].content}")

if __name__ == "__main__":
    chat("What is the risk level for GlobalTech Solutions?")
    chat("What is the SLA uptime guarantee in the contract?")
    chat("Summarize GlobalTech Solutions including their spend and contract termination rules.")
