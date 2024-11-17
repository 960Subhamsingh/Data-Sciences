import streamlit as st
import pandas as pd  # pip install pandas openpyxl

import plotly.express as px
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)


iris_df = px.data.iris()

st.subheader("Iris Dataset")

st.dataframe(iris_df)
 
# create the scatter plot using plotly express
basic_scatter_fig = px.scatter(iris_df, x="sepal_width", y ="sepal_length" , color="species", size="petal_length", symbol= "species")

# display the figure in streamlit
st.subheader("Iris Dataset : Basic Scatter Plot")
st.plotly_chart(basic_scatter_fig)

#user axis selection

x_axis = st.selectbox('Choose a variable for the x-axis ', iris_df.columns, index=0)
y_axis = st.selectbox('Choose a variable for the y-axis ', iris_df.columns, index=1) 

# create  bubble chart with color, differnt sysmbols, and hover data
colored_bouble_hover_fig = px.scatter(iris_df, x =y_axis , y =y_axis , color=
                                      'species', size='petal_length', hover_data=['petal_width']) 

# display the figure in Streamlit

st.subheader('iris DataSet: Bubble chart with Electable Axex')

colored_bouble_hover_fig.update_annotations(
  font_family= "Courier New",
  title = 'Iris Dataset Bubble Chart',
  xaxix_title = x_axis,
  yaxix_title = y_axis,
  legend_title= 'Species'
)

st.plotly_chart(colored_bouble_hover_fig)

chart_type = st.radio("select  chart type: " , ("Scatter plot","line char","Bar Char", "Histogram","Box Plot", "Pie Chart" , "3D Scatter plot"))

# Visualize the relationship betwween sepal length and sepal width , colered by species

if (chart_type == 'Scatter plot'):
  fig= px.scatter(iris_df , x='sepal_length' , y='sepal_width', color='species', title='Iris Scatter plot' )
  st.plotly_chart(fig) 

elif (chart_type == 'line char'):
  iris_df_sorted = iris_df.sort_values(by='sepal_length').reset_index()
  fig= px.line(iris_df_sorted, x=iris_df_sorted.index , y='sepal_length' , color='species', title='Iris sepal length Line Chart')
  st.plotly_chart(fig)

elif (chart_type == 'Bar Char'):
  avg_sepal_length = iris_df.groupby('species')['sepal_length'].mean().reset_index()
  fig = px.bar(avg_sepal_length , x='species', y='sepal_length', title= ' Average Sepal Length of Iris Species')
  st.plotly_chart(fig)

elif (chart_type == 'Histogram'):
   
  fig = px.histogram(iris_df, x='sepal_length', title="Sepal Length Distribution")
  st.plotly_chart(fig)

elif (chart_type == 'Box Plot'):
  fig = px.box(iris_df, x='species', y='sepal_length', title="Average Sepal Length of Iris Species")
  st.plotly_chart(fig)

elif (chart_type == 'Pie Chart'):
  species_count = iris_df['species'].value_counts().reset_index()
  fig = px.pie(species_count, names='species', values='species_id', title="Iris Speies Distrbution")
  st.plotly_chart(fig)

elif (chart_type == '3D Scatter plot'):
  fig = px.scatter(iris_df, x='sepal_length', y='sepal_width', color='species' ,title="3D Scatter plot Iris")
  st.plotly_chart(fig)

 