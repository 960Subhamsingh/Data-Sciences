import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
dates = pd.date_range('2024-01-01', periods=100)

data = pd.DataFrame(
    {
    'date': dates,
    'value': np.random.randn(100).cumsum()  # Cumulative sum of random values for illustration
})

st.write(data)
# Set the date as the index
data.set_index('date', inplace=True)

st.area_chart(data)

# Bar_chart

# Sample data
data = {
    'Category': ['A', 'B', 'C'],
    'Values': [10, 20, 30]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the bar chart
st.bar_chart(df)


# Line chart

st.line_chart(df)

# Pyplot Chart

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

# Map

## Create a sample DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060]
})
 
## Create a map with the data
st.map(data)

#  altair chart

import altair as alt

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)


# plotly_chart

import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)