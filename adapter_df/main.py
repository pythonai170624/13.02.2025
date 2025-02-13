from csv_loader import load_csv
from sqlite_loader import create_sqlite_db
from df_statistics import DataFrameStatistics
from sqlite_adapter import AdapterSQLitetoDF
from sqlite_statistics import SQLiteStatistics

def show_statistics(statistics_data):
    print("Averages:\n", statistics_data.calculate_averages())
    print("Std Deviation:\n", statistics_data.calculate_std_deviation())
    print("Duplicates:\n", statistics_data.find_duplicates())
    print("Missing Values:\n", statistics_data.calculate_missing_values())

def main():
    # Example 1: CSV
    print("=== CSV Example ===")
    df = load_csv("grades.csv")
    csv_statistics = DataFrameStatistics(df)
    show_statistics(csv_statistics)

    conn = create_sqlite_db()
    cursor = conn.cursor()

    # Example 2: SQLite Direct Statistics
    # print("\n=== SQLite Example with Adapter ===")
    # print("\n=== SQLite Example with Direct Statistics ===")
    # sqlite_statistics = SQLiteStatistics(conn, "sales")
    # show_statistics(sqlite_statistics)

    # # Example 3: SQLite with Adapter
    cursor.execute("SELECT * FROM sales")
    sqlite_result = [dict(record) for record in cursor.fetchall()]
    print(sqlite_result)
    sqlite_statistics_adapter = AdapterSQLitetoDF(sqlite_result)
    show_statistics(sqlite_statistics_adapter)



if __name__ == "__main__":
    main()
