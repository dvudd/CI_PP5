import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_prediction import page_prediction_body
from app_pages.page_correlation import page_correlation_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_ML_performance import page_ML_performance_body


app = MultiPage(app_name= "Heritage Housing Issues") # Create an instance of the app 

# load pages scripts
app.add_page("Project Summary", page_summary_body)
app.add_page("Predict House Prices", page_prediction_body)
app.add_page("Pricing Correlation", page_correlation_body)
app.add_page("Project Hypothesis and Validation", page_hypothesis_body)
app.add_page("ML Performance", page_ML_performance_body)


app.run() # Run the  app