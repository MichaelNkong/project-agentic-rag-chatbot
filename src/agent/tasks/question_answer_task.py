from crewai import Task
from src.agent.agents.question_answer_agent import qa_agent
from pydantic import BaseModel
from typing import List


class AnswerStructure(BaseModel):
    answer: str
    sources: List[str]
    tool_used: str
    rationale: str
qa_task = Task(
    description="""
You MUST answer using ONLY the provided context.

CHAT HISTORY:
{chat_history}

USER QUERY:
{query}

CONTEXT:
{context}

SOURCES:
{sources}
""",
    agent=qa_agent,
    expected_output="""
JSON with:
- answer
- sources
- tool_used
- rationale
""",
    output_pydantic=AnswerStructure
)