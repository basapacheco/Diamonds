import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use the environment variable for the data directory
data_dir = os.getenv('BBDDs_PATH')

def load_data(file_name):
    file_path = os.path.join(data_dir, file_name)
    return pd.read_csv(file_path)

if __name__ == "__main__":
    diamonds_train = load_data('diamonds_train.csv')
    diamonds_test = load_data('diamonds_test.csv')
    sample_submission = load_data('sample_submission.csv')
    print("First 5 rows of diamonds_train.csv:")
    print(diamonds_train.head())
    print("\nFirst 5 rows of diamonds_test.csv:")
    print(diamonds_test.head())
    print("\nFirst 5 rows of sample_submission.csv:")
    print(sample_submission.head())
    