import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use the environment variable for the data directory
data_dir = os.getenv('BBDDs_PATH')

def explore_data(df):
    print(df.describe())
    sns.pairplot(df)
    plt.show()

if __name__ == "__main__":
    diamonds_train = pd.read_csv(os.path.join(data_dir, 'diamonds_train.csv'))
    explore_data(diamonds_train)
