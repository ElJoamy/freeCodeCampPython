import unittest
import pandas as pd
from matplotlib import pyplot as plt
from os import path
import time_series_visualizer  # Asume que este es el nombre del módulo donde has guardado tus funciones

class TestDataVisualization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load data once for all tests"""
        cls.df = time_series_visualizer.load_and_clean_data()

    def setUp(self):
        """Initialize before every test."""
        print("\nStarting a test:", self.shortDescription())

    def tearDown(self):
        """Clean up after every test."""
        if self._outcome.success:
            print("Test passed!")
        else:
            print("Test failed!")

    def test_load_and_clean_data(self):
        """Test the data loading and cleaning function."""
        self.assertFalse(self.df.empty)
        self.assertTrue('value' in self.df.columns)

    def test_draw_line_plot(self):
        """Test the line plot function saves a figure correctly and has correct labels and title."""
        fig = time_series_visualizer.draw_line_plot(self.df)
        ax = fig.axes[0]
        self.assertTrue(isinstance(fig, plt.Figure))
        self.assertEqual(ax.get_title(), 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Page Views')
        self.assertTrue(path.exists('Visualizador de vistas de página en determinados períodos de tiempo/imgs/line_plot.png'))
        self.assertTrue(path.exists('Visualizador de vistas de página en determinados períodos de tiempo/examples/Figure_1.png'))

    def test_draw_bar_plot(self):
        """Test the bar plot function saves a figure correctly and has correct labels and legend."""
        fig = time_series_visualizer.draw_bar_plot(self.df)
        ax = fig.axes[0]
        self.assertTrue(isinstance(fig, plt.Figure))
        self.assertEqual(ax.get_xlabel(), 'Years')
        self.assertEqual(ax.get_ylabel(), 'Average Page Views')
        legend = ax.get_legend()
        self.assertEqual(legend.get_title().get_text(), 'Months')
        self.assertEqual([text.get_text() for text in legend.get_texts()], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        self.assertTrue(path.exists('Visualizador de vistas de página en determinados períodos de tiempo/imgs/bar_plot.png'))
        self.assertTrue(path.exists('Visualizador de vistas de página en determinados períodos de tiempo/examples/Figure_2.png'))

    def test_draw_box_plot(self):
        """Test the box plot function saves a figure correctly and has correct titles and labels."""
        fig = time_series_visualizer.draw_box_plot(self.df)
        ax_year, ax_month = fig.axes
        self.assertTrue(isinstance(fig, plt.Figure))
        self.assertEqual(ax_year.get_title(), 'Year-wise Box Plot (Trend)')
        self.assertEqual(ax_year.get_xlabel(), 'Year')
        self.assertEqual(ax_year.get_ylabel(), 'Page Views')
        self.assertEqual(ax_month.get_title(), 'Month-wise Box Plot (Seasonality)')
        self.assertEqual(ax_month.get_xlabel(), 'Month')
        self.assertEqual(ax_month.get_ylabel(), 'Page Views')
        self.assertEqual([label.get_text() for label in ax_month.get_xticklabels()], ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
        self.assertTrue(path.exists('Visualizador de vistas de página en determinados períodos de tiempo/imgs/box_plot.png'))
        self.assertTrue(path.exists('Visualizador de vistas de página en determinados períodos de tiempo/examples/Figure_3.png'))

if __name__ == '__main__':
    unittest.main()
