from ucimlrepo import fetch_ucirepo
import pandas as pd

census_income = fetch_ucirepo(id=20)

X = census_income.data.features
y = census_income.data.targets

data = pd.concat([X, y], axis=1)

# 1. Number of people per race
def race_counts():
    return data['race'].value_counts()

# 2. Average age of men
def average_age_men():
    return round(data[data['sex'] == 'Male']['age'].mean(), 1)

# 3. Percentage with Bachelors
def percentage_bachelors():
    return round((data['education'] == 'Bachelors').mean() * 100, 1)

# 4. Percentage of people with higher education earning >50K
def rich_percentage_higher_education():
    higher_education = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    return round((data[higher_education]['income'] == '>50K').mean() * 100, 1)

# 5. Percentage of people without higher education earning >50K
def rich_percentage_lower_education():
    low_education = ~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    return round((data[low_education]['income'] == '>50K').mean() * 100, 1)

# 6. Minimum hours per week
def min_work_hours():
    return int(data['hours-per-week'].min())

# 7. Percentage of people working minimum hours and earning >50K
def rich_percentage_min_hours():
    num_min_workers = data[data['hours-per-week'] == min_work_hours()]
    return round((num_min_workers['income'] == '>50K').mean() * 100, 1)

# 8. Highest earning country and percentage
def highest_earning_country():
    country_salary_rich = (data[data['income'] == '>50K']['native-country'].value_counts() / data['native-country'].value_counts())
    return country_salary_rich.idxmax(), round(country_salary_rich.max() * 100, 1)

# 9. Most popular occupation for those who earn >50K in India
def top_IN_occupation():
    return data[(data['native-country'] == 'India') & (data['income'] == '>50K')]['occupation'].mode()[0]
