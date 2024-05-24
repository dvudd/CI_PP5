import streamlit as st

def page_prediction_body():

    st.write("### Predict House Prices")

    st.warning(
        f"* A page displaying the 4 houses' attributes and their respective predicted sale price. It should display a message informing the summed predicted price for all 4 inherited houses. You should add interactive input widgets that allow a user to provide real-time house data to predict the sale price."
    )