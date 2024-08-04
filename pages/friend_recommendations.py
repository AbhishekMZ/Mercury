import streamlit as st
import pandas as pd
import ast

def display_top_matches():
    st.title("Introducing your top 3 potential friends for life!")

    # Load the CSV file
    file_path = 'C:/Users/KRITI KANNAN/Mercury/Responses_Matches.csv'
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        df.dropna(subset=['Top Matches'],inplace=True)
        # Assuming the last column contains the list of top matches
        if not df.empty and 'Top Matches' in df.columns:
            # Get the top matches for the first user (or change index as needed)
            top_matches_data = df.iloc[0]['Top Matches']

            # Check if the data is NaN
            if pd.isna(top_matches_data):
                st.write("No top matches available for the selected entry.")
                return

            # Print the type and content of top_matches_data for debugging
            st.write(f"Type of 'Top Matches': {type(top_matches_data)}")
            st.write(f"Content of 'Top Matches': {top_matches_data}")

            # Try to process the data based on its type
            if isinstance(top_matches_data, str):
                try:
                    # Safely evaluate the string to a Python list
                    top_matches = ast.literal_eval(top_matches_data)
                except Exception as e:
                    st.write(f"Error evaluating string data: {e}")
                    return
            elif isinstance(top_matches_data, list):
                top_matches = top_matches_data
            else:
                st.write("Unexpected data format in 'Top Matches' column.")
                return

            # Display the top matches
            for i, match in enumerate(top_matches[:3], start=1):
                st.write(f"*Match {i}*")
                st.write(f" {match.upper()}")  # Since match is now just a name string
                st.write("---")
        else:
            st.write("The 'Top Matches' column is not found or the file is empty.")
    except FileNotFoundError:
        st.write(f"The file '{file_path}' was not found.")
    except Exception as e:
        st.write(f"An error occurred: {e}")

display_top_matches()