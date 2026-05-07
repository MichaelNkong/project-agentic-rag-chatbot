
from src.agent.tasks.question_answer_task import qa_task
from src.agent.agents.question_answer_agent import qa_agent
from crewai import Crew

from src.rag_doc_ingestion.ingest_docs import ensure_vector_db
from src.tools.rag_query_tool import rag_query_tool
class CrewOrchestrator:

   def run_rag(self, query: str, chat_history: list):
        print("STARTING RAG")
        ensure_vector_db()
        raw = rag_query_tool(query)
        print("RAW TOOL RESULT:", raw)

        # 1. Normalize
        result = raw

        print("NORMALIZED RESULT:", result)

        if not result.get("has_context", False):
            return {
                "answer": "The knowledge source does not contain the required information.",
                "sources": [],
                "tool_used": "rag_query_tool",
                "rationale": "No relevant context found"
            }

        # 3. Inject context into task
        crew = Crew(
            agents=[qa_agent],
            tasks=[qa_task],
            verbose=True
        )
        output = crew.kickoff(
            inputs={
                "query": query,
                "context": result["answer"],
                "sources": result["sources"],
                "chat_history": chat_history  # 👈 ADD THIS
            }
        )

        return output


if __name__ == "__main__":
    execute_crew = CrewOrchestrator()
    print(execute_crew.run_rag("list me three cloud providers"))