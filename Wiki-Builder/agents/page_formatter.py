from crewai import Agent
from langchain_openai import ChatOpenAI
import os

def create_page_formatter():
    """Creates the Page Formatter agent to generate final Wikipedia-style articles"""
    backstory = (
        "You are a Wikipedia formatting specialist. "
        "Produce articles with markdown headings exactly as in this example:\n\n"
        "# Cryptocurrency\n\n"
        "## Background\n\nContent text...\n\n"
        "## History\n\nContent text...\n\n"
        "### Early Developments\n\nContent text...\n\n"
        "## Technology\n\nContent text...\n\n"
        "### Blockchain Basics\n\nContent text...\n\n"
        "## Impact\n\nContent text...\n"
        "\nUse # for main title, ## for main sections, and ### for subsections." \
        "For each main section (## Heading), place a horizontal rule (---) after the heading before any content or further information notes. Use _Further information:_ ... for subtle notes under headers as Wikipedia does. "
        "No extra commentary or notes, only article content. "
        "Ensure each section has meaningful, well-written text."
    )

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.5,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    return Agent(
        role="Page Formatter",
        goal="Transform organized summaries into polished, Wikipedia-style articles with proper formatting",
        backstory=backstory,
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
