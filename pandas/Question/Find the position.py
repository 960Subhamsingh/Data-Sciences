# Find the position of the second occurrence of "e". You can do this by using Python’s string methods or applying a custom function with apply().

import pandas as pd

# Sample DataFrame
data = {'O': ['apple', 'elephant', 'eagle', 'beetle', 'cherry']}
df = pd.DataFrame(data)

# Function to find the second occurrence of 'e' and extract the substring
def extract_before_second_e(s):
    # Find all occurrences of 'e' in the string
    indices = [i for i, char in enumerate(s) if char == 'e']
    
    # If there are at least two occurrences of 'e', extract the substring
    if len(indices) >= 2:
        return s[:indices[1]]  # Substring up to the second 'e'
    else:
        return s  # If no second 'e', return the whole string

# Apply the function to the 'O' column
df['extracted'] = df['O'].apply(extract_before_second_e)

print(df)
