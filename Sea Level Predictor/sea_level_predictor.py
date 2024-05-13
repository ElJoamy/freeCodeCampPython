import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def load_data():
    df = pd.read_csv('Sea Level Predictor/epa-sea-level.csv')
    return df

def draw_scatter_plot(df):
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    return plt

def draw_line_of_best_fit(df):
    plt = draw_scatter_plot(df)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, 'r')
    print("Line of best fit X values:", x_pred.tolist())
    print("Line of best fit Y values:", y_pred.tolist())
    return plt

def draw_line_of_best_fit_2000(df):
    plt = draw_line_of_best_fit(df)
    new_df = df[df['Year'] >= 2000]
    res_new = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x_new_pred = pd.Series([i for i in range(2000, 2051)])
    y_new_pred = res_new.intercept + res_new.slope * x_new_pred
    plt.plot(x_new_pred, y_new_pred, 'g')
    print("Line of best fit from 2000 X values:", x_new_pred.tolist())
    print("Line of best fit from 2000 Y values:", y_new_pred.tolist())
    return plt

def save_plot(plt):
    plt.savefig('Sea Level Predictor/imgs/sea_level_plot.png')
    plt.show()

if __name__ == '__main__':
    df = load_data()
    plt = draw_line_of_best_fit_2000(df)
    save_plot(plt)
