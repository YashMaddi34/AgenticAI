from google.adk.agents.llm_agent import Agent, LlmAgent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    """Blueprint for email outputs"""
    subject: str = Field(
        description="Concise, descriptive subject line (5-10 words)"
    )
    body: str = Field(
        description="Formatted content with greeting, paragraphs, and signature"
    )




root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='I can provide email content based on your requirements',
    instruction="You're an email assistant, Generate an email based on users input ONLY with a JSON object containing the subject and body. Format: {\"subject\": \"Email Subject\", \"body\": \"Email Body\"}",
    output_schema=EmailContent,
    output_key='email'
)
