import pandas as pd

def demographic_data_analyzer():
    # Load the dataset
    df = pd.read_csv('adult.csv')

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    advanced_education_over_50K = (advanced_education & (df['salary'] == '>50K')).mean() * 100

    # 5. What percentage of people without advanced education make more than 50K?
    no_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    no_advanced_education_over_50K = (no_advanced_education & (df['salary'] == '>50K')).mean() * 100

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_work_hours_salary = df[df['hours-per-week'] == min_work_hours]
    min_work_hours_over_50K = (min_work_hours_salary['salary'] == '>50K').mean() * 100

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_percentage = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = country_percentage.max()

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_earnings = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    most_popular_occupation_india = india_earnings['occupation'].value_counts().idxmax()

    # Return results as a dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'advanced_education_over_50K': advanced_education_over_50K,
        'no_advanced_education_over_50K': no_advanced_education_over_50K,
        'min_work_hours': min_work_hours,
        'min_work_hours_over_50K': min_work_hours_over_50K,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'most_popular_occupation_india': most_popular_occupation_india
    }
