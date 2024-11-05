import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine

# title
st.title("This is title ")

# header
st.header("Theis is a header with a divider", divider="gray")
st.header("this is a header :blue[cool]:sunglass")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is a simple text")
# Write
st.write("This is written in text")
st.write("1 + 1 = ", 2)

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

data = pd.DataFrame({"first column": [1, 2, 3, 4],"second column": [10, 20, 30, 40]})

st.write(df.head())
st.write(data)

# Markdown
st.markdown("# This is a Markdown heading")
st.markdown("[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)")
st.markdown("This is a Markdown paragraph with **bold** and *italic* text")

st.markdown("""
        1. step 1
        2. step 2
            
        - unordered step 1
        - step 2
            - substep 2.1    
""")

# Emojis
st.markdown("### Emojis")
st.markdown("[Emojis](https://share.streamlit.io/streamlit/emoji-shortcodes)")
st.markdown("Here are some emojis:")
st.markdown(":thumbsup: :heart: :rocket: :smile: :taurus:")

# HTML
st.markdown("### HTML")
html_code = """
        <h1 style='color: blue;'>This is a blue heading</h1>
        <p style='color: green;'>This is a green paragraph</p>
"""
st.markdown(html_code, unsafe_allow_html=True)

# Divider
st.markdown("""---""")
st.divider()

# LaTeX
st.write("LaTex")

st.latex(r"e^{i\pi} + 1 = 0")
st.latex(r"f(x) = x^2 + 2x + 1")
st.latex(r"g(x) = \frac{1}{x}")
st.latex(r"h(x) = \sqrt{x}")
st.latex(r"y = mx + c")
st.latex(r"a^2 + b^2 = c^2")

iris = load_iris()

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df["FlowerType"] = [iris.target_names[target] for target in iris.target]

st.write(iris_df.head(5))

wine = load_wine()

wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[target] for target in wine.target]

st.write(wine_df[['alcohol','malic_acid']].head())

