import streamlit as st

def page_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    st.success(
        f"### Quality\n"
        f"Validated through a correlation study.\n"
        f"* Findings indicate that the overall quality and kitchen quality of a house significantly"
        f"influence the sale price.\n"
        f"### Size\n"
        f"Validated through a correlation study.\n"
        f"* Results show that larger above-ground living areas and garage sizes positively impact the"
        f"sale price.\n"
        f"### Age\n"
        f"Validated through a correlation study.\n"
        f"* The property's age has an effect on its sale price. This indicates that the construction"
        f"date of both the house and garage has an impact on the sale price of the property.\n"
    )