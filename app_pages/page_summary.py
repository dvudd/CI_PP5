import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    # Text based on README file - "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"* The dataset is sourced from"
        f" [Kaggle](https://www.kaggle.com/datasets/codeinstitute/"
        f"housing-prices-data).\n"
        f"* The dataset has almost 1.5 thousand rows and represents housing"
        f"records from Ames, Iowa, indicating house profile (Floor Area,"
        f"Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and"
        f"its respective sale price for houses built between 1872 and 2010."
    )

    # Link to README
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/dvudd/CI_PP5/).")

    # Copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house"
        f"attributes correlate with the sale price. Therefore, the client"
        f"expects data visualisations of the correlated variables against the"
        f"sale price to show that.\n"
        f"* 2 - The client is interested in predicting the house sale price"
        f"from her four inherited houses and any other house in Ames, Iowa."
        )
