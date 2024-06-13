import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    diamonds_train = load_data('../BBDDs/diamonds_train.csv')
    print(diamonds_train.head())
