import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_processing import load_and_process_data
from visualizations import (
    plot_state_delivery_counts,
    plot_monthly_delivery_counts,
    plot_route_type_distribution
)
from hypothesis_testing import (
    test_actual_vs_osrm_distance,
    test_actual_vs_osrm_time,
    test_monthly_delivery_counts
)

def main():
    st.title("Delhivery Data Analysis Dashboard")

    # Load and process data
    df = load_and_process_data()

    # Sidebar for navigation
    page = st.sidebar.selectbox("Choose a page", ["Overview", "Visualizations", "Hypothesis Testing"])

    if page == "Overview":
        st.header("Data Overview")
        st.write(df.head())
        st.write(df.describe())

    elif page == "Visualizations":
        st.header("Data Visualizations")

        st.subheader("State-wise Delivery Counts")
        fig_state = plot_state_delivery_counts(df)
        st.pyplot(fig_state)

        st.subheader("Monthly Delivery Counts")
        fig_month = plot_monthly_delivery_counts(df)
        st.pyplot(fig_month)

        st.subheader("Route Type Distribution")
        fig_route = plot_route_type_distribution(df)
        st.pyplot(fig_route)

    elif page == "Hypothesis Testing":
        st.header("Hypothesis Testing Results")

        st.subheader("Actual vs OSRM Distance")
        result_distance = test_actual_vs_osrm_distance(df)
        st.write(result_distance)

        st.subheader("Actual vs OSRM Time")
        result_time = test_actual_vs_osrm_time(df)
        st.write(result_time)

        st.subheader("Monthly Delivery Counts (9th vs 10th month)")
        result_monthly = test_monthly_delivery_counts(df)
        st.write(result_monthly)

if __name__ == "__main__":
    main()