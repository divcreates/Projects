from crewai import Agent
from langchain_openai import ChatOpenAI
import os

def create_summarizer():
    """Creates the Summarizer agent to organize and structure data"""

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.5,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    return Agent(
        role="Summarizer",
        goal="Organize and summarize extracted data into structured, logical sections for Wikipedia-style content",
        backstory="""You are an expert content organizer who takes raw research data and transforms it into 
        well-structured summaries. You identify key themes, chronological events, and important concepts, 
        then organize them into logical sections that will form the backbone of a Wikipedia article. 
        You ensure information flows logically and all important aspects are covered.
        Group facts into major sections, each with a suggested heading.”""",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
