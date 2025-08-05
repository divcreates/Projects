from crewai import Agent
from crewai_tools import WebsiteSearchTool
from langchain_openai import ChatOpenAI
import os

def create_data_extractor():
    """Creates the Data Extractor agent to fetch facts from the web (max 3-4 searches)"""

    # Use CrewAI’s built-in WebsiteSearchTool
    search_tool = WebsiteSearchTool()

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.3,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    backstory = (
        "You are a Data Extractor. "
        "When tasked with researching a topic, you must perform **no more than 3-4 distinct web searches**. "
        "Each search should be concise and focused on gathering key factual information. "
        "Do not exceed three queries. Return the raw snippets from each search."
    )

    return Agent(
        role="Data Extractor",
        goal="Gather raw factual data from the web with at most three searches",
        backstory=backstory,
        llm=llm,
        tools=[search_tool],
        verbose=True,
        allow_delegation=False
    )


