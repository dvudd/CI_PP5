import joblib


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)