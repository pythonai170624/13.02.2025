from grades_statistics_builder import GradesStatisticsBuilder
from sales_statistics_builder import SalesStatisticsBuilder
from grades_data_sample import GradesDataSample
from sales_data_sample import SalesDataSample

if __name__ == "__main__":
    # Example for grades
    grades_path = "grades.csv"  # Replace with your grades CSV file
    grades_builder = GradesStatisticsBuilder(GradesDataSample, grades_path)
    grades_data_sample = grades_builder.build()
    print("=== Grades Data Sample ===")
    print(grades_data_sample)
    print("Missing Values:\n", grades_data_sample.missing_values)
    print("Duplicates:\n", grades_data_sample.duplicates)

    # Example for sales
    sales_path = "sales.csv"  # Replace with your sales CSV file
    sales_builder = SalesStatisticsBuilder(SalesDataSample, sales_path)
    sales_data_sample = sales_builder.build()
    print("\n=== Sales Data Sample ===")
    print(sales_data_sample)
    print("Missing Values:\n", sales_data_sample.missing_values)
    print("Duplicates:\n", sales_data_sample.duplicates)
