# crew.py - Multi-agent Wikipedia Builder with proper CrewAI implementation

from crewai import Crew, Task, Process
from agents import create_data_extractor, create_summarizer, create_page_formatter

def run_crew(topic):
    """
    Runs the 3-agent CrewAI system to generate a Wikipedia-style article

    Agent Flow:
    1. Data Extractor → Searches web for information about the topic
    2. Summarizer → Organizes the extracted data into structured sections  
    3. Page Formatter → Creates the final polished Wikipedia article
    """

    try:
        # Create the 3 agents
        data_extractor = create_data_extractor()
        summarizer = create_summarizer()
        page_formatter = create_page_formatter()

        # TASK 1: Data Extraction
        extraction_task = Task(
            description=f"""Search the web thoroughly for information about '{topic}'. 

            Extract comprehensive information including:
            - Historical background and origins
            - Key events, dates, and milestones  
            - Important figures and their roles
            - Current status and developments
            - Significant facts and statistics
            - Cultural, social, or scientific impact

            Use your web search tool to gather factual, verifiable information from multiple sources.
            Only perform up to 3 web searches to gather facts.
            Organize your findings clearly with specific details, dates, and facts.
            Keep each search result concise and relevant.
            """,

            expected_output=f"Comprehensive research data about {topic} including historical facts, key events, important figures, dates, and current information gathered from web sources.",

            agent=data_extractor
        )

        # TASK 2: Data Summarization and Organization
        summarization_task = Task(
            description=f"""Take the extracted data about '{topic}' and organize it into a structured summary.

            Create a logical structure with these sections:
            - Introduction/Overview
            - Background/Origins  
            - Historical Development
            - Key Features/Characteristics
            - Impact and Significance
            - Current Status/Modern Developments

            For each section, provide:
            - 2-3 key points with specific details
            - Important dates and figures
            - Relevant facts and context

            Organize the information logically and ensure smooth flow between sections.""",

            expected_output=f"Well-organized summary of {topic} divided into logical sections with key points, dates, figures, and facts ready for article formatting.",

            agent=summarizer,
            context=[extraction_task]
        )

        # TASK 3: Wikipedia Article Formatting
        formatting_task = Task(
            description=f"""Transform the organized summary into a complete Wikipedia-style article about '{topic}'.

            FORMAT REQUIREMENTS:
            - Start with topic name as main heading
            - Use ## for main sections (Background, History, Features, Impact, etc.)
            - Use ### for subsections when needed
            - Write in neutral, encyclopedic tone
            - Each section should have 2-4 substantial paragraphs
            - Include specific dates, names, and facts
            - Minimum 800 words total

            ARTICLE STRUCTURE:
            # {topic}

            [Opening paragraph with definition and overview]

            ## Background
            [2-3 paragraphs about origins and foundational information]

            ## History
            [2-3 paragraphs about historical development]

            ## [Additional relevant sections based on topic]

            CRITICAL: Return ONLY the formatted Wikipedia article. No meta-commentary or explanations about the article.""",

            expected_output=f"Complete Wikipedia-style article about {topic} with proper markdown formatting, comprehensive content, and encyclopedic tone - article text only.",

            agent=page_formatter,
            context=[summarization_task]
        )

        # Create and execute the crew
        crew = Crew(
            agents=[data_extractor, summarizer, page_formatter],
            tasks=[extraction_task, summarization_task, formatting_task],
            process=Process.sequential,
            verbose=True
        )

        # Execute the crew and get results
        result = crew.kickoff()

        # Extract the final article content
        if hasattr(result, 'raw'):
            content = result.raw
        elif hasattr(result, 'result'):
            content = result.result  
        elif isinstance(result, str):
            content = result
        else:
            content = str(result)

        return content.strip()

    except Exception as e:
        error_msg = f"Error in multi-agent crew execution: {str(e)}"
        print(error_msg)
        return error_msg

# Test function for debugging
def test_crew():
    """Test function to verify the crew works"""
    print("🧪 Testing the 3-agent CrewAI system...")
    result = run_crew("Python Programming Language")
    print(f"✅ Result length: {len(result)} characters")
    return result

if __name__ == "__main__":
    test_crew()
