CPS Data Cleaning and Analysis (Chicago Public Schools)

This project demonstrates essential data cleaning, feature engineering, and statistical analysis techniques using the Chicago Public Schools (CPS) dataset.

The script performs the following key operations:

Data Cleaning & Feature Engineering

New Feature Creation: Extracts Lowest_Grade and Highest_Grade from the Grades_Offered_All column.

Complex Data Extraction: Uses a custom function (extract_start_hour) to parse School_Hours and convert the starting time into a 24-hour integer format (Starting_Hour).

Missing Value Imputation: Replaces missing numerical values (NaN) in key columns (Student_Count_Total, College_Enrollment_Rate_School, Starting_Hour) with the respective column means.

Statistical Analysis

The script calculates and prints:

Mean and standard deviation for College Enrollment Rate in High Schools.

Mean and standard deviation for Student Count in Non-High Schools.

The frequency distribution of school starting hours.

The total count of schools located outside the defined Loop Neighborhood ZIP codes.

How to Run the Code

Dataset: Ensure the cps.csv file is available in the same directory.

Dependencies: Install Pandas (pip install pandas).

Execute: Run the script from the terminal: python student_dataset.py
