import unittest
import sea_level_predictor
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class TestSeaLevelPredictor(unittest.TestCase):

    def setUp(self):
        """Initialize before every test."""
        print("\nStarting a test:", self.shortDescription())
        self.df = sea_level_predictor.load_data()

    def tearDown(self):
        """Clean up after every test."""
        if self._outcome.success:
            print("Test passed!")
        else:
            print("Test failed!")

    def test_load_data(self):
        """Ensure data is loaded correctly and contains expected columns."""
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertFalse(self.df.empty)
        self.assertIn('Year', self.df.columns)
        self.assertIn('CSIRO Adjusted Sea Level', self.df.columns)

    def test_scatter_plot_elements(self):
        """Check scatter plot for correct labels and title."""
        plt = sea_level_predictor.draw_scatter_plot(self.df)
        ax = plt.gca()
        self.assertEqual(ax.get_title(), 'Rise in Sea Level')
        self.assertEqual(ax.get_xlabel(), 'Year')
        self.assertEqual(ax.get_ylabel(), 'Sea Level (inches)')

    def test_line_of_best_fit(self):
        """Verify that the line of best fit is correct and extends to 2050."""
        plt = sea_level_predictor.draw_line_of_best_fit(self.df)
        ax = plt.gca()
        lines = ax.get_lines()
        x_data, y_data = lines[0].get_data()
        self.assertTrue(min(x_data) <= self.df['Year'].min() and max(x_data) >= 2050)

    def test_line_of_best_fit_2000(self):
        """Check the second line of best fit from 2000 to 2050."""
        plt = sea_level_predictor.draw_line_of_best_fit_2000(self.df)
        ax = plt.gca()
        lines = ax.get_lines()
        x_data, y_data = lines[1].get_data()
        self.assertTrue(min(x_data) >= 2000 and max(x_data) >= 2050)

    def test_data_points(self):
        """Verify the plot includes correct data points."""
        plt = sea_level_predictor.draw_scatter_plot(self.df)
        ax = plt.gca()
        scatter = ax.collections[0]
        self.assertEqual(len(scatter.get_offsets()), len(self.df))

if __name__ == '__main__':
    unittest.main()
