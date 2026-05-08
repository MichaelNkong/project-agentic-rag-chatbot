import logging

from src.agent.crew_orchestration import CrewOrchestrator
import json
logger = logging.getLogger(__name__)
crewOrchestrator = None
def get_answer(chat_history: list) -> dict:
    global crewOrchestrator
    if crewOrchestrator is None:
        crewOrchestrator = CrewOrchestrator()
    logger.info(f"Received chat_history: {chat_history}")
    # get the last message in the chat_history as user_query
    last_user_message = chat_history[-1]
    user_query = last_user_message["content"]
    logger.info(f"Extracted user_query: {user_query}")
    # Remove the last user message from chat_history
    history_without_last = chat_history[:-1]
    logger.debug(f"Input data for qa_crew: {chat_history}")
    result = crewOrchestrator.run_rag(user_query,history_without_last)
    # Case 1: already parsed dict
    if hasattr(result, "raw"):
        raw = result.raw

        if isinstance(raw, str):
            return json.loads(raw)

        if isinstance(raw, dict):
            return raw
    # Case 2: CrewAI object with raw
    if isinstance(result, dict):
        return result



  #Example usage
if __name__ == "__main__":
  sample_chat_history = [
     {"role": "user", "content": "What is Evolution?"},
     {"role": "assistant", "content": "Evolution is the scientific theory describing how all life forms on Earth change over successive generations through alterations in their genetic material, leading to the diversity of life seen today. This process involves changes in an organism's genetic makeup (genome), which result from processes like mutation and are influenced by natural selection, where individuals with advantageous traits for their environment leave more offspring."},
    {"role": "user", "content": "What is restful API"}
  ]
  response = get_answer(sample_chat_history)
  print("final result is",response)
