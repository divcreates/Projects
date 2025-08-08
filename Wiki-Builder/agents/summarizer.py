from crewai import Agent
from langchain_openai import ChatOpenAI
import os

def create_summarizer():
    """Creates the Summarizer agent to organize and structure data for Wikipedia-style content"""

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.5,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    return Agent(
        role="Summarizer",
        goal="Organize and summarize extracted data into clear, well-structured sections for Wikipedia-style content",
        backstory=(
            "You are an expert content organizer. "
            "Your job is to take raw extracted data (often messy or unordered) and transform it into a clear, structured summary. "
            "Group related facts under logical section headings (e.g., Background, History, Technology, Impact). "
            "Maintain a neutral tone. Organize events chronologically where applicable, and ensure smooth logical flow. "
            "This summary will be passed to a Wikipedia-style formatter — so it must be clean, grouped, and complete. "
            "Avoid lists of bullets unless necessary — use full paragraphs."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
