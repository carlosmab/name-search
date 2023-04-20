import os
import psycopg2
from contextlib import contextmanager
from dotenv import load_dotenv
from app.services.db_connection.db_connection import DBConnection


load_dotenv()


class PostgreSQLConnection(DBConnection):
    def __init__(self, db_name: str, user: str, password: str, host: str, port: str):
        self.db_name: str = db_name
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.port: str = port
        
    def set_params_from_env(self) -> None:
        self.db_name = os.environ.get("POSTGRES_DB_NAME", "")
        self.user = os.environ.get("POSTGRES_USER", "")
        self.password = os.environ.get("POSTGRES_PASSWORD", "")
        self.host = os.environ.get("POSTGRES_HOST", "")
        self.port = os.environ.get("POSTGRES_PORT", "")
    
    def connect(self) -> None:
        self.connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def close(self) -> None:
        self.cursor.close()
        self.connection.close()

    # NOTE: This method was generated using "ChatGPT 3" it could lead to 
    #   potential security risks or be outdated. 
    #   Carefully review and validate the performance
    @contextmanager
    def connection_context(self):
        """
            Context manager for handling the database connection.
        """
        try:
            self.connect()
            yield self
        finally:
            self.close()