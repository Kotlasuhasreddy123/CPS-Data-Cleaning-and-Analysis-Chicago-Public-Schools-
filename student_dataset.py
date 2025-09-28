import pandas as pd

def main():
    # 1. Load the cps.csv file
    cps = pd.read_csv("cps.csv")

    # 2. Build the required dataframe 

    # select existing columns (make sure names match file)
    df = cps[['School_ID', 'Short_Name', 'Is_High_School',
              'Zip', 'Student_Count_Total', 'College_Enrollment_Rate_School']].copy()

    # Lowest grade offered (first grade in Grades_Offered_All string)
    df['Lowest_Grade'] = cps['Grades_Offered_All'].str.split(',').str[0].str.strip()

    # Highest grade offered (last grade in Grades_Offered_All string)
    df['Highest_Grade'] = cps['Grades_Offered_All'].str.split(',').str[-1].str.strip()

    # Starting Hour – extract the hour number from School_Hours (e.g. '8:00AM-3:00PM')
    def extract_start_hour(hours):
        if pd.isna(hours):
            return None
        # Take text before dash, split at ':' and convert to float hour
        start = hours.split('-')[0].strip()
        try:
            hour = int(start.split(':')[0])
        except:
            return None
        # adjust for PM if present and not 12
        if 'PM' in start and hour != 12:
            hour += 12
        return hour

    df['Starting_Hour'] = cps['School_Hours'].apply(extract_start_hour)

    # Replace missing numeric values with column means
    num_cols = ['Student_Count_Total', 'College_Enrollment_Rate_School', 'Starting_Hour']
    for col in num_cols:
        mean_val = df[col].mean(skipna=True)
        df[col] = df[col].fillna(mean_val)

    # Display first 10 rows
    print("\nFirst 10 rows of cleaned DataFrame:")
    print(df.head(10))

    # 3a. Mean & std of College Enrollment Rate for High Schools
    hs = df[df['Is_High_School'] == True]
    print("\nCollege Enrollment Rate (High Schools):")
    print("Mean:", round(hs['College_Enrollment_Rate_School'].mean(), 2))
    print("Std :", round(hs['College_Enrollment_Rate_School'].std(), 2))

    # 3b. Mean & std of Student_Count_Total for non-High Schools
    non_hs = df[df['Is_High_School'] == False]
    print("\nStudent Count (Non-High Schools):")
    print("Mean:", round(non_hs['Student_Count_Total'].mean(), 2))
    print("Std :", round(non_hs['Student_Count_Total'].std(), 2))

    # 3c. Distribution of starting hours
    print("\nDistribution of Starting Hours:")
    print(df['Starting_Hour'].value_counts().sort_index())

    # 3d. Number of schools outside the Loop Neighborhood
    loop_zips = {60601,60602,60603,60604,60605,60606,60607,60616}
    outside_loop = df[~df['Zip'].isin(loop_zips)]
    print("\nNumber of schools outside Loop Neighborhood:", outside_loop.shape[0])

if __name__ == "__main__":
    main()
