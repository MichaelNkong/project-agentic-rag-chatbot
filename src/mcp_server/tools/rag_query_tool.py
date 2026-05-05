from crewai.tools import tool
from langchain_community.chat_models import ChatOpenAI

from src.agent.config.agent_settings import AgentSettings


settings = AgentSettings()
vector_db = settings.load_vector_db()

# 👇 LLM added (keep temperature low for RAG)
llm = ChatOpenAI(
    model = settings.MODEL_NAME,
    temperature = settings.model_temperature
)


def rag_query_tool(query: str) -> dict:
    """Retrieve relevant context and sources from the vector database.

    Returns:
        dict with keys:
        - has_context: bool
        - answer: str
        - sources: List[str]
    """
    print(">>> TOOL EXECUTED <<<")
    import logging

    logger = logging.getLogger(__name__)

    docs_and_scores = vector_db.similarity_search_with_score(query, k=5)

    threshold = 1.0

    relevant_docs = [
        (doc, score) for doc, score in docs_and_scores if score < threshold
    ]

    logger.info(f"Query: {query}")
    logger.info(f"Top 5 scores: {[score for _, score in docs_and_scores]}")
    logger.info(f"Filtered scores: {[score for _, score in relevant_docs]}")

    if not relevant_docs:
        return {
            "has_context": False,
            "answer": "The knowledge source does not contain the required information.",
            "sources": []
        }

    logger.info(f"Query: {query}")
    logger.info(f"Top 5 similarity scores: {[score for _, score in docs_and_scores[:5]]}")
    logger.info(f"Relevant docs (score < {threshold}): {len(relevant_docs)}")

    context = "\n\n".join([doc.page_content for doc, _ in relevant_docs])
    sources = [doc.metadata.get("source", "unknown") for doc, _ in relevant_docs]

    logger.info(f"Found {len(relevant_docs)} relevant documents")

    # 👇 NEW: LLM STEP (keeps your structure unchanged)
    prompt = f"""
You are a precise assistant. Use ONLY the context below to answer.

Context:
{context}

Question:
{query}

Rules:
- Only use provided context
- If context is insufficient, say "The knowledge source does not contain the required information."
- Be concise and factual
"""

    response = llm.invoke(prompt)

    return {
        "has_context": True,
        "answer": response.content,   # 👈 now LLM-generated
        "sources": sources
    }


if __name__ == "__main__":
    print(rag_query_tool("what is an ecosystem"))