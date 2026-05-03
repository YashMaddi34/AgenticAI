from google.adk.agents.llm_agent import Agent, LlmAgent
from pydantic import BaseModel, Field

from datetime import date

class TodoItem(BaseModel):
    task: str = Field(description="Task name")
    due_date: date = Field(description="YYYY-MM-DD format")
    priority: str = Field(description="low/medium/high")

root_agent = LlmAgent(
    name="todo_agent",
    model="gemini-2.0-flash",
    instruction="""Generate todo items in exact JSON format"\
        Make sure the format if follwows this structure: {"task": "Task name", "due_date": "YYYY-MM-DD", "priority": "low/medium/high"}""",
    output_schema=TodoItem,
    output_key="todo"
)

# Example usage
# todo = todo_agent.run("Create high-priority task to call client today")
# print(f"Task: {todo['todo']['task']}")
# print(f"Due: {todo['todo']['due_date']}")
