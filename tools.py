import os
from crewai_tools import SerperDevTool, WebsiteSearchTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define tools
search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))

web_search_tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-pro",
                temperature=0.7,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        ),
    )
)
