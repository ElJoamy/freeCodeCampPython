import unittest
import medical_data_visualizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestMedicalDataVisualizer(unittest.TestCase):
    def setUp(self):
        """Initialize before every test."""
        print("\nStarting a test:", self.shortDescription())
        self.df = medical_data_visualizer.load_data()
        self.df = medical_data_visualizer.add_overweight_column(self.df)
        self.df = medical_data_visualizer.normalize_data(self.df)

    def tearDown(self):
        """Clean up after every test."""
        if self._outcome.success:
            print("Test passed!")
        else:
            print("Test failed!")

    def test_load_data(self):
        """Test if data is loaded properly."""
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertFalse(self.df.empty)

    def test_add_overweight_column(self):
        """Test if 'overweight' column is added correctly."""
        self.assertIn('overweight', self.df.columns)
        self.assertTrue(all(self.df['overweight'].isin([0, 1])))

    def test_normalize_data(self):
        """Test if data is normalized correctly."""
        self.assertTrue(all(self.df['cholesterol'].isin([0, 1])))
        self.assertTrue(all(self.df['gluc'].isin([0, 1])))

    def test_draw_cat_plot(self):
        """Test if categorical plot is generated correctly."""
        fig = medical_data_visualizer.draw_cat_plot(self.df)
        self.assertIsInstance(fig, plt.Figure)
        axes = fig.get_axes()
        self.assertEqual(len(axes), 2) 
        for ax in axes:
            expected_labels = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
            actual_labels = [text.get_text() for text in ax.get_xticklabels()]
            self.assertEqual(actual_labels, expected_labels)

    def test_draw_heat_map(self):
        """Test if heatmap is generated correctly."""
        fig = medical_data_visualizer.draw_heat_map(self.df)
        self.assertIsInstance(fig, plt.Figure)
        ax = fig.get_axes()[0]
        expected_labels = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        actual_labels = [label.get_text() for label in ax.get_xticklabels()]
        self.assertEqual(actual_labels, expected_labels)

    def test_clean_data(self):
        """Test if data cleaning removes inappropriate rows."""
        df_original = self.df.copy()
        df_clean = medical_data_visualizer.clean_data(self.df)
        self.assertTrue(len(df_clean) <= len(df_original))
        self.assertTrue(all(df_clean['ap_lo'] <= df_clean['ap_hi']))

if __name__ == '__main__':
    unittest.main()
