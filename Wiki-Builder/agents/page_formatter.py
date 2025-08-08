from crewai import Agent
from langchain_openai import ChatOpenAI
import os

def create_page_formatter():
    """Creates the Page Formatter agent to generate final Wikipedia-style articles"""

    backstory = (
        "You are a Wikipedia article formatting expert. "
        "Your task is to format well-organized summaries into clean, polished Wikipedia-style Markdown. "
        "Follow the example strictly:\n\n"

        "# Cryptocurrency\n\n"
        "## Background\n\n"
        "---\n"
        "Content text...\n\n"
        "## History\n\n"
        "---\n"
        "_Further information: Early developments of crypto_\n\n"
        "### Early Developments\n\n"
        "Content text...\n\n"
        "## Technology\n\n"
        "---\n"
        "_Further information: How blockchain works_\n\n"
        "### Blockchain Basics\n\n"
        "Content text...\n\n"
        "## Impact\n\n"
        "---\n"
        "Content text...\n\n"

        "Rules:\n"
        "- Use `#` for the main title (only once).\n"
        "- Use `##` for main sections and insert a horizontal rule (`---`) after each `## Heading`.\n"
        "- Use `_Further information:_` under `##` headings where necessary (max 1 line).\n"
        "- Use `###` for any relevant subsections.\n"
        "- Never include personal notes, comments, or explanations. Only return the article.\n"
        "- Each section must be well-written, fact-rich, and structured."
    )

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.5,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    return Agent(
        role="Page Formatter",
        goal="Transform structured summaries into a clean, Wikipedia-style article with proper Markdown formatting",
        backstory=backstory,
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
