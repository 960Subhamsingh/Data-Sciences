import streamlit as st
import time

# Title
st.title("Streamlit Status and Progress Indicator Examples")

st.header("1. Basic Progress Bar")
st.text("Streamlit has a built-in st.progress function that allows you to show a simple progress bar. This can be useful when you have a long-running task and want to inform users about the progress.")
st.title("Streamlit Progress Bar Example")

# Create a progress bar
progress_bar = st.progress(0)

# Simulate a long-running task
for i in range(1, 101):
    time.sleep(0.1)  # Simulating a task
    progress_bar.progress(i)  # Update the progress bar

st.success("Task Completed!")


# Progress
st.subheader("Progress Bar")
progress_bar = st.progress(0)
status_text = st.empty()
for i in range(101):
    time.sleep(0.05)
    progress_bar.progress(i)
    status_text.text(f"Progress: {i}%")
status_text.text("Progress: Done!")


st.header("2. Status Messages with st.spinner")
st.text("something that takes a few seconds, you can use st.spinner to display a loading spinner while your task is running. This is great for showing that something is happening in the background.")

st.title("Streamlit Spinner Example")

with st.spinner('Processing...'):
    time.sleep(5)  # Simulating a task

st.success('Processing Complete!')


st.header("3. Status with st.empty (Dynamic Status Update)")
st.text("st.empty() to dynamically update a placeholder in the app. This can be useful to show real-time status updates or intermediate results during a task.")

# Create a placeholder for dynamic updates
status_placeholder = st.empty()

# Simulate a long-running task with status updates

for i in range(1,11):
    status_placeholder.text(f"Step {i}/10: Processing..")
    time.sleep(1)
status_placeholder.text("Task Completed")


st.title("4. Combined Progress Bar and Spinner")
st.text("combine the spinner with a progress bar to indicate both the status of the task (with the spinner) and the progress (with the bar).")
# Create a progress bar
progress_bar = st.progress(0)

# Show a spinner during the task
with st.spinner('Please wait...'):
    for i in range(1, 101):
        time.sleep(0.1)  # Simulating work
        progress_bar.progress(i)  # Update progress bar

st.success("Task Completed Successfully!")

st.header("combine the spinner with a progress bar to indicate both the status of the task (with the spinner) and the progress (with the bar).")

st.text("interactive status indicator, you can show the progress of file uploads or other processes that involve interaction.")

uploaded_file = st.file_uploader("Choose a file", type="csv")

if uploaded_file is not None:
    status_placeholder = st.empty()  # Placeholder for progress updates
    progress_bar = st.progress(0)
    
    # Simulate file processing
    total_steps = 10
    for i in range(total_steps):
        status_placeholder.text(f"Processing file... Step {i + 1}/{total_steps}")
        progress_bar.progress((i + 1) * 100 // total_steps)
        time.sleep(0.5)  # Simulate time taken by each step
    
    status_placeholder.text("File processed successfully!")
    st.balloons()  # Celebrate completion



st.header("6. Show Multiple Status Updates with st.empty()")
st.text("You can use st.empty() for more complex status updates where the message or component might change over time.")

st.title("Multiple Status Updates Example")

# Create multiple placeholders for different status updates
step1_placeholder = st.empty()
step2_placeholder = st.empty()
step3_placeholder = st.empty()

# Simulate different steps of a task
step1_placeholder.text("Step 1: Initializing...")
time.sleep(2)
step1_placeholder.text("Step 1: Initialization complete!")

step2_placeholder.text("Step 2: Processing...")
time.sleep(3)
step2_placeholder.text("Step 2: Processing complete!")

step3_placeholder.text("Step 3: Finalizing...")
time.sleep(2)
step3_placeholder.text("Step 3: Finalization complete!")

st.success("Task Completed Successfully!")

st.header("7. Using st.progress with a Timer")
st.text("If you want to simulate a countdown or progress over a set time, you can use the st.progress method with a timer for more accurate control.")

st.title("Streamlit Timer Progress Example")

# Set the total time for the process (in seconds)
total_time = 10

# Create a progress bar
progress_bar = st.progress(0)

# Simulate a task with a timer
for i in range(total_time):
    progress_bar.progress((i + 1) * 100 // total_time)
    time.sleep(1)

st.success("Task Completed!")


# Status
st.subheader("Status")
st.status("This is a status message")

# Toast
st.subheader("Toast")
st.warning("This is a warning message")
st.error("This is an error message")
st.success("This is a success message")
st.info("This is an info message")

# Snow
st.subheader("Snow")
st.snow()

# Balloons
st.subheader("Balloons")
st.balloons()

# Success, error, warning, info
st.subheader("Different Alert Types")
st.success("Success alert message")
st.error("Error alert message")
st.warning("Warning alert message")
st.info("Info alert message")





