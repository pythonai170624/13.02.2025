import sqlite3
from abstract_statistics import AbstractStatistics

class SQLiteStatistics(AbstractStatistics):
    def __init__(self, conn, table_name):
        """
        Initialize with an SQLite connection and the table name.
        """
        self.conn = conn
        self.table_name = table_name

    def _get_numeric_columns(self):
        """
        Retrieve numeric columns from the table.
        """
        cursor = self.conn.cursor()
        cursor.execute(f"PRAGMA table_info({self.table_name})")
        columns = cursor.fetchall()
        numeric_columns = [col[1] for col in columns if col[2] in ('INTEGER', 'REAL')]
        return numeric_columns

    def calculate_averages(self):
        """
        Calculate the averages for numeric columns.
        """
        numeric_columns = self._get_numeric_columns()
        averages = {}
        cursor = self.conn.cursor()

        for column in numeric_columns:
            cursor.execute(f"SELECT AVG({column}) FROM {self.table_name}")
            averages[column] = cursor.fetchone()[0]
        return averages

    def calculate_std_deviation(self):
        """
        Calculate the standard deviation for numeric columns.
        """
        numeric_columns = self._get_numeric_columns()
        std_devs = {}
        cursor = self.conn.cursor()

        for column in numeric_columns:
            cursor.execute(f"""
            SELECT
                sqrt(sum((({column} * 1.0) - avg({column})) * 
                (({column} * 1.0) - avg({column}))) / 
                (count({column}) - 1))
            FROM {self.table_name}
            """)
            std_devs[column] = cursor.fetchone()[0]
        return std_devs

    def find_duplicates(self):
        """
        Identify duplicate rows based on all columns.
        """
        cursor = self.conn.cursor()
        cursor.execute(f"PRAGMA table_info({self.table_name})")
        columns = [col[1] for col in cursor.fetchall()]
        query = f"""
        SELECT *, COUNT(*) 
        FROM {self.table_name}
        GROUP BY {', '.join(columns)}
        HAVING COUNT(*) > 1
        """
        cursor.execute(query)
        duplicates = cursor.fetchall()
        return duplicates

    def calculate_missing_values(self):
        """
        Calculate the count of missing (NULL) values for each column.
        """
        cursor = self.conn.cursor()
        cursor.execute(f"PRAGMA table_info({self.table_name})")
        columns = [col[1] for col in cursor.fetchall()]
        missing_values = {}

        for column in columns:
            cursor.execute(f"SELECT COUNT(*) FROM {self.table_name} WHERE {column} IS NULL")
            missing_values[column] = cursor.fetchone()[0]
        return missing_values
