import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris, load_wine

# title
st.title("This is title ")
# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is a simple text")
# Write
st.write("This is written in text")

# Markdown
st.markdown("# This is a Markdown heading")
st.markdown("[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)")
st.markdown("This is a Markdown paragraph with **bold** and *italic* text")

iris = load_iris()

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df["FlowerType"] = [iris.target_names[target] for target in iris.target]

st.write(iris_df.head(10))

wine = load_wine()

wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[target] for target in wine.target]

st.write(wine_df[['alcohol','malic_acid']])

