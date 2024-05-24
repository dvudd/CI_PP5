import streamlit as st
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


def performance(x_train, y_train, x_test, y_test, pipeline):
    st.write("Model Evaluation \n")
    st.write("* Train Set")
    evaluation(x_train, y_train, pipeline)
    st.write("* Test Set")
    evaluation(x_test, y_test, pipeline)


def evaluation(x, y, pipeline):
    prediction = pipeline.predict(x)
    st.write('R2 Score:', r2_score(y, prediction).round(2))
    st.write('Mean Absolute Error:', mean_absolute_error(
        y, prediction).round(2))
    st.write('Mean Squared Error:', mean_squared_error(y, prediction).round(2))
    st.write('Root Mean Squared Error:', np.sqrt(
        mean_squared_error(y, prediction)).round(2))
    st.write("\n")
