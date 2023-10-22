class MySQLDatabase:
    def query(self, query_string):
        return f"Выполняем SQL-запрос в MySQL: {query_string}"

class PostgreSQLDatabase:
    def execute(self, query_string):
        return f"Выполняем SQL-запрос в PostgreSQL: {query_string}"

class DatabaseAdapter:
    def execute_query(self, query_string):
        pass

class MySQLAdapter(DatabaseAdapter):
    def __init__(self, mysql_db):
        self.mysql_db = mysql_db

    def execute_query(self, query_string):
        return self.mysql_db.query(query_string)

class PostgreSQLAdapter(DatabaseAdapter):
    def __init__(self, postgres_db):
        self.postgres_db = postgres_db

    def execute_query(self, query_string):
        return self.postgres_db.execute(query_string)

if __name__ == "__main__":
    mysql_db = MySQLDatabase()
    postgres_db = PostgreSQLDatabase()

    mysql_adapter = MySQLAdapter(mysql_db)
    postgres_adapter = PostgreSQLAdapter(postgres_db)

    query = "SELECT * FROM table_name"

    result1 = mysql_adapter.execute_query(query)
    result2 = postgres_adapter.execute_query(query)

    print(result1)
    print(result2)
