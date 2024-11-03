from typing import Any
from urllib.parse import urlparse

from langchain.agents import create_sql_agent, AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

from api.const import (
    LLM_MODEL,
    PG_URI
)


class QueryService:
    async def get_query(self, question, pg_uri = PG_URI) -> Any:
        try:
            if pg_uri.startswith('postgres://'):
                pg_uri = pg_uri.replace('postgres://', 'postgresql://', 1)

            llm = ChatOpenAI(temperature=0, model_name=LLM_MODEL)

            db = SQLDatabase.from_uri(
                pg_uri,
                sample_rows_in_table_info=3
            )

            db_chain = SQLDatabaseChain.from_llm(
                llm=llm,
                db=db,
                verbose=True,
                top_k=3
            )

            prompt = """ 
               Given an input question, create a syntactically correct postgresql query to run.
               Return only the SQL query without any markdown formatting, backticks, or sql tags.
               The question: {question}
               """

            return db_chain.run(prompt.format(question=question))
        except Exception as e:
            print(f"Error in get_query: {str(e)}")
            raise

    async def get_agent_query(self, question, pg_uri=PG_URI) -> Any:
        try:
            if pg_uri.startswith('postgres://'):
                pg_uri = pg_uri.replace('postgres://', 'postgresql://', 1)

            llm = ChatOpenAI(temperature=0, model_name=LLM_MODEL)
            db = SQLDatabase.from_uri(pg_uri)
            toolkit = SQLDatabaseToolkit(db=db, llm=llm)

            agent_executor = create_sql_agent(
                llm=llm,
                toolkit=toolkit,
                verbose=True,
                agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            )

            return agent_executor.run(question)
        except Exception as e:
            print(f"Error in get_agent_query: {str(e)}")
            raise