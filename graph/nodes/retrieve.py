from graph.state import GraphState
from ingestion import retriever
from typing import Dict, Any

def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")

    question = state["question"]
    documents = retriever.invoke("question")

    return {"question":question, "documents":documents}