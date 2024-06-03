import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate import performance, evaluation


def page_ML_performance_body():
    """
    This function loads the trained machine learning pipeline and its
    evaluation results, including feature importance and performance plots,
    and displays them in a Streamlit app. It also shows the pipeline steps and
    the features used for training the model.
    """
    version = 'v1'
    model = load_pkl_file(f"outputs/ml_pipeline/{version}/pipeline.pkl")
    evalplot = plt.imread(f"outputs/ml_pipeline/{version}/evaluation_plot.png")
    feat = plt.imread(f"outputs/ml_pipeline/{version}/features_importance.png")
    x_train = pd.read_csv(f"outputs/ml_pipeline/{version}/x_train.csv")
    x_test = pd.read_csv(f"outputs/ml_pipeline/{version}/x_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/{version}/y_train.csv").values
    y_test = pd.read_csv(f"outputs/ml_pipeline/{version}/y_test.csv").values

    st.write("### ML Performance")

    # Pipeline
    st.write("---")
    st.write("* The pipeline that was used in this project:")
    st.write(model)

    # Feature importance plot
    st.write("---")
    st.write("### Feature Importance Plot")
    st.write("* The features the model was trained and their importance.")
    st.write(x_train.columns.to_list())
    st.image(feat)

    # Evaluation
    st.write("---")
    st.write("### Pipeline Performance")
    performance(x_train, y_train, x_test, y_test, model)
    st.text("")

    # Performance plot
    st.write("### Pipeline Performance Plots")
    st.image(evalplot)
