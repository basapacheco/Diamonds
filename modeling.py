import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use the environment variable for the data directory
data_dir = os.getenv('BBDDs_PATH')

def preprocess_data(df):
    df['volume'] = df['x'] * df['y'] * df['z']  
    df = df.drop(['x', 'y', 'z'], axis=1)  
    df = pd.get_dummies(df, columns=['cut', 'color', 'clarity'], drop_first=True)  
    return df

def train_model(df):
    X = df.drop('price', axis=1)
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ('scaler', StandardScaler()),  
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))  
    ])

    param_grid = {
        'model__n_estimators': [100, 200, 300],
        'model__max_depth': [None, 10, 20, 30]
    }

    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    return grid_search.best_estimator_, grid_search.best_params_

if __name__ == "__main__":
    diamonds_train = pd.read_csv(os.path.join(data_dir, 'diamonds_train.csv'))
    diamonds_train = preprocess_data(diamonds_train)
    model, best_params = train_model(diamonds_train)
    print(f"Best model parameters: {best_params}")

