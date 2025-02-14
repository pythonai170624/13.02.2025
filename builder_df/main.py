from statistics_builder_grades import GradesStatisticsBuilder
from statistics_builder_sales import SalesStatisticsBuilder

if __name__ == "__main__":
    # Example for grades
    grades_path = "grades.csv"
    grades_builder = GradesStatisticsBuilder(grades_path)
    grades_data_sample = grades_builder.build()
    print("=== Grades Data Sample ===")
    print(grades_data_sample)
    print("Missing Values:\n", grades_data_sample.missing_values)
    print("Duplicates:\n", grades_data_sample.duplicates)

    # Example for sales
    sales_path = "sales.csv"
    sales_builder = SalesStatisticsBuilder(sales_path)
    sales_data_sample = sales_builder.build()
    print("\n=== Sales Data Sample ===")
    print(sales_data_sample)
    print("Missing Values:\n", sales_data_sample.missing_values)
    print("Duplicates:\n", sales_data_sample.duplicates)
