import unittest
import pandas as pd
from demographic_data_analyzer import (
    data, 
    race_counts, 
    average_age_men, 
    percentage_bachelors, 
    rich_percentage_higher_education, 
    rich_percentage_lower_education, 
    min_work_hours, 
    rich_percentage_min_hours, 
    highest_earning_country, 
    top_IN_occupation
)

class DemographicDataAnalyzerTest(unittest.TestCase):
    def setUp(self):
        """Initialize before every test."""
        print("\nStarting a test:", self.shortDescription())

    def tearDown(self):
        """Clean up after every test."""
        if self._outcome.success:
            print("Test passed!")
        else:
            print("Test failed!")

    def test_data_frame(self):
        """Test data is a DataFrame."""
        self.assertIsInstance(data, pd.DataFrame)

    def test_race_counts(self):
        """Test race counts are returned as a Series."""
        result = race_counts()
        self.assertIsInstance(result, pd.Series)
        self.assertTrue('White' in result.index)

    def test_average_age_men(self):
        """Test average age of men is calculated correctly."""
        result = average_age_men()
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)

    def test_percentage_bachelors(self):
        """Test percentage of bachelors is calculated correctly."""
        result = percentage_bachelors()
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)

    def test_rich_percentage_higher_education(self):
        """Test percentage with higher education earning >50K."""
        result = rich_percentage_higher_education()
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)

    def test_rich_percentage_lower_education(self):
        """Test percentage without higher education earning >50K."""
        result = rich_percentage_lower_education()
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)

    def test_min_work_hours(self):
        """Test minimum working hours are calculated correctly."""
        result = min_work_hours()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)

    def test_rich_percentage_min_hours(self):
        """Test percentage earning >50K among minimum hours workers."""
        result = rich_percentage_min_hours()
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)

    def test_highest_earning_country_and_percentage(self):
        """Test highest earning country and percentage are identified correctly."""
        country, percentage = highest_earning_country()
        self.assertIsInstance(country, str)
        self.assertIsInstance(percentage, float)
        self.assertGreaterEqual(percentage, 0)
        self.assertLessEqual(percentage, 100)

    def test_top_IN_occupation(self):
        """Test most popular occupation among >50K earners in India is identified correctly."""
        result = top_IN_occupation()
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
