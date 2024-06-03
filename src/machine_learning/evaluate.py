import streamlit as st
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


def performance(x_train, y_train, x_test, y_test, pipeline):
    """
    This function evaluates the performance of a trained machine learning
    pipeline on both the training and test datasets, displaying the evaluation
    metrics in a Streamlit app.
    """
    st.write("Model Evaluation \n")
    st.write("* Train Set")
    evaluation(x_train, y_train, pipeline)
    st.write("* Test Set")
    evaluation(x_test, y_test, pipeline)


def evaluation(x, y, pipeline):
    """
    This function predicts the target values using the provided pipeline and
    input samples, then calculates and displays the R2 score, mean absolute
    error, mean squared error, and root mean squared error using Streamlit.
    """
    prediction = pipeline.predict(x)
    st.write('R2 Score:', r2_score(y, prediction).round(2))
    st.write('Mean Absolute Error:', mean_absolute_error(
        y, prediction).round(2))
    st.write('Mean Squared Error:', mean_squared_error(y, prediction).round(2))
    st.write('Root Mean Squared Error:', np.sqrt(
        mean_squared_error(y, prediction)).round(2))
    st.write("\n")
