import pandas as pd
import plotly.express as px
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use the environment variable for the data directory
data_dir = os.getenv('BBDDs_PATH')

def visualize_data(df):
    fig = px.scatter(df, x='carat', y='price', color='cut', title='Carat vs Price by Cut')
    fig.show()

if __name__ == "__main__":
    diamonds_train = pd.read_csv(os.path.join(data_dir, 'diamonds_train.csv'))
    visualize_data(diamonds_train)
