import streamlit as st
import pandas  as pd
import matplotlib.pyplot as plt

# Add a title and intro text
st.title('Upload file with user')
st.text('This is a web app to allow exploration of Earth')

# Create File uploader object 

upload_file = st.file_uploader('Upload a file containig earthquake data')

# Check to see if a file has been uploaded
if upload_file is not None:
    # If it has then do the following:
    
    # Read the file to a dataframe using pandas 
    df = pd.read_csv(upload_file)

    # Create a section for the dataframe  statistics
    st.header('Statistics of Dataframe show onl for the numberic columns')
    st.write(df.describe())

    # Create a section for the dataframe header
    st.header('Show the top 5 Rows in existing data file')
    st.write(df.head())

     # Create a section for matplotlib figure
    st.header('Plot of Data')
    
    
    # plt.scatter(x=df['Depth'], y=df['Magnitude'])
    # plt.xlabel('Depth')
    # plt.ylabel('magnitudde')

    fig , ax = plt.subplots(  )
    ax.scatter(x= df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    
    st.pyplot(fig )

