import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "Visualizador de vistas de página en determinados períodos de tiempo"

def load_and_clean_data():
    df = pd.read_csv(f'{path}/fcc-forum-pageviews.csv', index_col="date", parse_dates=True)
    df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]
    return df

def draw_line_plot(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.savefig(f'{path}/imgs/line_plot.png')
    plt.savefig(f'{path}/examples/Figure_1.png')
    return fig

def draw_bar_plot(df):
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_pivot = df.pivot_table(values='value', index='year', columns='month', aggfunc='mean')

    fig, ax = plt.subplots(figsize=(10, 6))
    df_pivot.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.savefig(f'{path}/imgs/bar_plot.png')
    plt.savefig(f'{path}/examples/Figure_2.png')
    return fig

def draw_box_plot(df):
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df, ax=axes[1], order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    plt.savefig(f'{path}/imgs/box_plot.png')
    plt.savefig(f'{path}/examples/Figure_3.png')
    return fig

if __name__ == '__main__':
    df = load_and_clean_data()
    draw_line_plot(df)
    draw_bar_plot(df)
    draw_box_plot(df)