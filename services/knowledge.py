import os
from agno.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.embedder.openai import OpenAIEmbedder

def get_knowledge_base():
    vector_db = LanceDb(
        table_name="textbooks",
        uri="tmp/lancedb",
        search_type=SearchType.vector,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    )
    knowledge_base = Knowledge(
        vector_db=vector_db,
        path="data",
    )

    return knowledge_base
