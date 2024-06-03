import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import load_house_data


def page_correlation_body():
    """
    This function loads the housing data, displays various data insights, and
    shows the correlation of different house features with the sale price
    using both Pearson and Spearman correlation methods. It provides options
    for users to inspect the housing data, view correlation bar plots, and
    compare Pearson vs. Spearman correlations.
    """
    # Load data
    df = load_house_data()

    # Mapping dictionaries for each feature
    BsmtExposure_map = {'None': 0, 'No': 0, 'Mn': 1, 'Av': 2, 'Gd': 3}
    BsmtFinType1_map = {
        'GLQ': 6, 'ALQ': 5, 'BLQ': 4,
        'Rec': 3, 'LwQ': 2, 'Unf': 1, 'None': 0
    }
    GarageFinish_map = {'Fin': 3, 'RFn': 2, 'Unf': 1, 'None': 0}
    KitchenQual_map = {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1, 'Po': 0}

    st.write("### Pricing Correlation Study")
    st.text("")
    st.info(
        # Copied from README file - "Business Requirements" section
        f"* Business requirement 1 - The client is interested in discovering "
        f"how the house attributes correlate with the sales prices. "
        f"Therefore, the client expects data visualizations "
        f"of the correlated variables against the sale price.")

    # Inspect data
    if st.checkbox("Inspect Housing Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f"\nThese are the first 10 rows:")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better "
        f"understand how the variables are correlated to the house's sale "
        f"price.\n"
    )

    # Conclusions
    st.success(
        f"The price of a property is directly correlated with its quality and"
        f" size, as well as its construction date."
    )

    # Pearson Correlation
    pearson_corr = df.corr(method='pearson')['SalePrice'].sort_values(
        key=abs, ascending=False
        )
    pearson_corr = pearson_corr.drop('SalePrice')
    if st.checkbox("Pearson Correlation"):
        barplot_corr(df=pearson_corr)

    # Spearman Correlation
    spearman_corr = df.corr(method='spearman')['SalePrice'].sort_values(
        ascending=False
        )
    spearman_corr = spearman_corr.drop('SalePrice')
    if st.checkbox("Spearman Correlation"):
        barplot_corr(df=spearman_corr)

    # Comparison
    if st.checkbox("Comparison"):
        compare_corr(pearson_corr, spearman_corr)


def barplot_corr(df):
    """
    This function creates and displays a bar plot of the correlation
    coefficients between various house features and the sale price using
    Seaborn and Matplotlib. The plot is displayed in a Streamlit app.
    """
    plt.figure(figsize=(10, 8))
    sns.barplot(x=df.index, y=df.values, palette='viridis')
    plt.xticks(rotation=90)
    plt.title('Spearman Correlation with SalePrice')
    plt.xlabel('Features')
    plt.ylabel('Correlation Coefficient')
    st.pyplot(plt)


def compare_corr(pearson_corr, spearman_corr):
    """
    This function creates a scatter plot to compare Pearson and Spearman
    correlation coefficients of house features with the sale price. It also
    highlights features with high correlation coefficients and displays the
    plot in a Streamlit app.
    """
    # Define the threshold
    threshold = 0.5

    correlation_comparison = pd.DataFrame({
        'Pearson': pearson_corr,
        'Spearman': spearman_corr
    })

    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='Pearson', y='Spearman', data=correlation_comparison)
    plt.title('Comparison of Pearson vs. Spearman Correlations')
    plt.xlabel('Pearson Correlation Coefficient')
    plt.ylabel('Spearman Correlation Coefficient')

    plt.axhline(threshold, color='red', linestyle='--', linewidth=1)
    plt.axvline(threshold, color='red', linestyle='--', linewidth=1)

    for line in range(0, correlation_comparison.shape[0]):
        plt.text(
            correlation_comparison.Pearson[line]+0.01,
            correlation_comparison.Spearman[line],
            correlation_comparison.index[line],
            horizontalalignment='left',
            size='medium',
            color='black',
            weight='semibold'
            )

    plt.grid(True)
    plt.show()
    st.pyplot(plt)

    pearson_features = pearson_corr[abs(pearson_corr) > threshold]
    spearman_features = spearman_corr[abs(spearman_corr) > threshold]

    result = list(
        set(
            pearson_features.index.to_list()) | set(
                spearman_features.index.to_list())
        )
    st.write(result)
