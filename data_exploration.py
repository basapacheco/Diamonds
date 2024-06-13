import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def explore_data(df):
    print(df.describe())
    sns.pairplot(df)
    plt.show()

if __name__ == "__main__":
    diamonds_train = pd.read_csv('../BBDDs/diamonds_train.csv')
    explore_data(diamonds_train)
