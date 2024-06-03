import streamlit as st
import pandas as pd
from src.data_management import (
    load_pkl_file,
    load_inherited_data,
    load_house_data
    )
from src.machine_learning.predict_house_prices import (
    single_house_prediction,
    inherited_house_prediction
    )


def page_prediction_body():
    """
    This function sets up a Streamlit page to allow users to input data for a
    single house and get a predicted sale price using a pre-trained model.
    It also provides functionality to predict the sale prices of multiple
    inherited houses and displays the combined total predicted sale price.
    The function uses interactive widgets to collect user inputs and display
    the predictions.
    """
    version = 'v1'
    model = load_pkl_file(f"outputs/ml_pipeline/{version}/pipeline.pkl")
    features = (pd.read_csv(
        f"outputs/ml_pipeline/{version}/x_train.csv").columns.to_list())

    # Inherited House Price Predictions
    st.write("### Sale Price Prediction Interface - Inherited Houses")
    st.text("")

    st.info(
        # Copied from README file - "Business Requirements" section
        f"* Business requirement 2 - The client is interested in predicting"
        f" the house sale prices from\n"
        f"her 4 inherited houses, and any other house in Ames, Iowa."
    )

    df_inherited = load_inherited_data()

    # Display inherited houses data
    if st.checkbox("Inspect Inherited Housing Data"):
        st.write(df_inherited)

    st.text("")

    # Predict inherited houses data
    if st.button("Run Predictive Analysis on Inherited Houses"):
        st.write(
            sale_price_prediction=inherited_house_prediction(
                df_inherited, features, model)
        )

    st.write("---")

    st.write("### Sale Price Prediction Interface - Single House")
    st.text("")

    # Single House Price Predictions
    df_single = input_widget()

    # Button for single house price prediction
    st.text("")
    if st.button("Run Predictive Analysis on Single House"):
        sale_price_prediction = single_house_prediction(
            df_single, features, model)


def input_widget():
    """
    This function sets up a Streamlit interface with interactive widgets for
    users to input data for a single house's features. The collected data is
    then stored in a DataFrame which can be used for making predictions.
    """

    # Load dataset
    df = load_house_data()

    # Create a empty DataFrame
    df_single = pd.DataFrame([], index=[0])

    # Widget Layout
    col4, col3, col1 = st.beta_columns(3)
    col2, col5 = st.beta_columns(2)

    # Populate widgets
    with col4:
        feature = "OverallQual"
        st_widget = st.number_input(
            label="Overall Quality",
            min_value=1,
            max_value=10,
            value=int(df[feature].median())
        )
    df_single[feature] = st_widget

    with col3:
        feature = "KitchenQual"
        st_widget = st.number_input(
            label="Kitchen Quality",
            min_value=1,
            max_value=5,
            value=int(df[feature].median())
        )
    df_single[feature] = st_widget

    with col1:
        feature = "GarageArea"
        st_widget = st.number_input(
            label="Garage Area",
            min_value=0,
            max_value=2836,
            value=int(df[feature].median())
        )
    df_single[feature] = st_widget

    with col2:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label="Above Ground Living Area",
            min_value=0,
            max_value=11284,
            value=int(df[feature].median())
        )
    df_single[feature] = st_widget

    with col5:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label="Total Basement Area",
            min_value=0,
            max_value=12220,
            value=int(df[feature].median())
        )
    df_single[feature] = st_widget

    return df_single
