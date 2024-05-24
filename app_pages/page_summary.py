import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # Text based on README file - "Dataset Content" section
    st.warning(
        f"* A project summary page, showing the project dataset summary and the client's requirements."
        )

    # Text based on README file - "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"* The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).\n"
        f"* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010."
    )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/dvudd/CI_PP5/).")
    

    # Copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.\n"
        f"* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa."
        )