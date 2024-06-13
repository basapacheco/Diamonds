import pandas as pd
import plotly.express as px

def visualize_data(df):
    fig = px.scatter(df, x='carat', y='price', color='cut', title='Carat vs Price')
    fig.show()

if __name__ == "__main__":
    diamonds_train = pd.read_csv('../BBDDs/diamonds_train.csv')
    visualize_data(diamonds_train)
