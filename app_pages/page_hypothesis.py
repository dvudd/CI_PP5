import streamlit as st


def page_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    st.write("#### Quality")
    st.success(
        f"Validated through a correlation study.\n"
        f"* Findings indicate that the overall quality and kitchen quality of"
        f" a house significantly influence the sale price.\n"
    )
    st.write("#### Size")
    st.success(
        f"Validated through a correlation study.\n"
        f"* Results show that larger above-ground living areas and garage"
        f" sizes positively impact the sale price.\n"
    )
    st.write("#### Age")
    st.success(
        f"Validated through a correlation study.\n"
        f"* The property's age has an effect on its sale price. This indicates"
        f" that the construction date of both the house and garage has an"
        f" impact on the sale price of the property.\n"
    )
