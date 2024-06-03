import joblib
import pandas as pd


def load_pkl_file(file_path):
    """
    Load a pickle file from the specified file path.
    """
    return joblib.load(filename=file_path)


def load_inherited_data():
    """
    Load and preprocess the inherited houses dataset.
    Replaces categorical values in the 'KitchenQual' column with numerical
    values, and returns the preprocessed DataFrame.
    """
    df = pd.read_csv("inputs/datasets/raw/inherited_houses.csv")
    df['KitchenQual'] = df['KitchenQual'].replace(
        {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1, 'Po': 0})
    return df


def load_house_data():
    """
    Load and preprocess the house prices dataset.
    Replaces categorical values in the 'KitchenQual' column with numerical
    values, and returns the preprocessed DataFrame.
    """
    df = pd.read_csv("outputs/datasets/collection/HousePrices.csv")
    df['KitchenQual'] = df['KitchenQual'].replace(
        {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1, 'Po': 0})
    return df
