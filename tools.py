import sqlite3
from langchain_core.tools import tool
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

@tool
def get_supplier_metrics(supplier_name: str) -> str:
    """Fetches financial and risk metrics for a supplier from the local ERP database."""
    conn = sqlite3.connect('procurement_erp.db')
    cursor = conn.cursor()
    cursor.execute("SELECT risk_level, total_spend FROM suppliers WHERE supplier_name = ?", (supplier_name,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return f"Supplier: {supplier_name} | Risk: {result[0]} | Spend: ${result[1]}"
    return "Not found in ERP."

embeddings = OllamaEmbeddings(model="nomic-embed-text")

def setup_rag():
    loader = TextLoader("data/supplier_contract_v1.txt")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    splits = splitter.split_documents(docs)
    
    db = Chroma.from_documents(splits, embeddings)
    return db.as_retriever()

retriever = setup_rag()

@tool
def search_contract(query: str) -> str:
    """Searches supplier contracts for clauses and terms."""
    docs = retriever.invoke(query)
    return "\n".join([d.page_content for d in docs])
