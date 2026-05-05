from crewai import Agent
from src.agent.llm.load_llm import get_llm_for_agent

qa_agent = Agent(
    role="Answer Formatter",
    llm=get_llm_for_agent("Question_Answer_Agent"),
    tools=[],
    allow_delegation=False,
    goal="Format provided context into structured JSON output.",
    backstory="You format already-verified retrieval results."
)