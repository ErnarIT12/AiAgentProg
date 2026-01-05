from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.db.sqlite import SqliteDb
import os
from dotenv import load_dotenv
from sqlalchemy.sql.functions import session_user

load_dotenv()

def calculate_tax(amount : int) -> str:
    return str(amount * 0.1)

def get_agent(session_id : str = None) -> Agent:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("API key is missing")
    return Agent(model = OpenAIChat(id = "gpt-3.5-turbo"),
                 description="Ты помощник, который помнит диалог.",
                 db = SqliteDb(db_file = "agent.db" ),
                 session_id= session_id,
                 tools = [calculate_tax],
                 markdown = True,
                 )


