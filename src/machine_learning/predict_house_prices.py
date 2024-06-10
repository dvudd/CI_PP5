import streamlit as st


def inherited_house_prediction(df, features, model):
    """
    Predict the sale prices of multiple properties using a pre-trained model.
    This function takes a dataframe containing property data, filters it to
    include only the specified features, and then uses the provided model to
    predict the sale prices of multiple properties. The predicted sale prices
    for each property and the total sale price for all properties combined are
    displayed using Streamlit.
    """
    # from live data, subset features related to this pipeline
    df_sale_price = df.filter(features)

    # prediction for each property
    sale_price_predictions = model.predict(df_sale_price)

    total_sale_price = 0

    for idx, prediction in enumerate(sale_price_predictions, start=1):
        sale_price = int(prediction)
        total_sale_price += sale_price
        st.write(
            f"* The predicted sale price of property"
            f"{idx} is ${sale_price:,}"
            )
    st.write(
        f"* **The predicted sale price of all properties combined is "
        f"${total_sale_price:,}**"
    )

    return sale_price_predictions


def single_house_prediction(df, features, model):
    """
    This function takes a dataframe containing property data, filters it to
    include only the specified features, and then uses the provided model to
    predict the sale price of a single property. The predicted sale price is
    displayed using Streamlit.
    """
    # from live data, subset features related to this pipeline
    subset = df.filter(features)

    # prediction for this property
    price_prediction = model.predict(subset)

    statement = (
            f"* The predictive value of this property is:"
            f" **${round(price_prediction[0])}**.\n"
            )

    st.write(statement)
