import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
import random

# Load data from the Responses.MBTI file
data = pd.read_csv('models/Responses.MBTI.csv')

# Check and fill missing 'Name' values with unique names
data['Name'] = data['Name'].apply(lambda x: x if pd.notna(x) and x.strip() else 'User_' + str(random.randint(1000, 9999)))

# Handle categorical data
categorical_columns = ['Gender', 'Branch', 'What\'s your preferred language for communication? (select all that apply)', 'MBTI Type', 'What type of hobbies are you primarily into?']
data['Gender'] = data['Gender'].apply(lambda x: 1 if x == "Male" else 0)
# Ensure categorical columns exist
for column in categorical_columns:
    if column not in data.columns:
        raise KeyError(f"Column '{column}' not found in the dataset")
    data[column] = data[column].fillna('Unknown')  # Fill missing values with 'Unknown'
    
# One-hot encode categorical columns (including 'Hobbies')
encoder = OneHotEncoder(sparse_output=False)  # Set sparse_output to False
encoded_data = encoder.fit_transform(data[categorical_columns])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_columns))

# Identify numerical columns
numerical_columns = [' Year of study']
numerical_data = data[numerical_columns]

# Standardize numerical data
scaler = StandardScaler()
numerical_data = pd.DataFrame(scaler.fit_transform(numerical_data), columns=numerical_columns)

# Combine numerical and encoded categorical data
processed_data = pd.concat([numerical_data.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)

# Compute cosine similarity
similarity_matrix = cosine_similarity(processed_data)

# Identify mentees (those who want a mentor)
mentees = data[data['Would you like a mentor'] == 'Yes']
# Identify potential mentors (who are senior)
mentors = data[data['Year of Study'] > data['Year of Study'].mean()]

# Generate recommendations
recommendations = {}

for i, mentee in mentees.iterrows():
    mentee_name = mentee['Name']
    mentee_year = mentee['Year of Study']
    
    # Filter potential mentors (must be senior)
    potential_mentors = mentors[mentors['Year of Study'] > mentee_year]
    
    # If no senior mentors, consider all mentors
    if potential_mentors.empty:
        potential_mentors = mentors
    
    mentee_index = data.index[data['Name'] == mentee_name][0]
    
    # Calculate similarity scores
    similarity_scores = similarity_matrix[mentee_index, potential_mentors.index]
    
    # Get top matches
    top_indices = np.argsort(similarity_scores)[-3:][::-1]  # Get the top 3 matches
    top_matches = potential_mentors.iloc[top_indices]['Name'].values
    
    recommendations[mentee_name] = top_matches.tolist()

# Ensure at least one match per individual
for mentee in mentees['Name']:
    if mentee not in recommendations:
        random_mentor = mentors.sample(1)['Name'].values[0]
        recommendations[mentee] = [random_mentor]

# Save recommendations to a new CSV file
recommendation_df = pd.DataFrame.from_dict(recommendations, orient='index').reset_index()
recommendation_df.columns = ['Mentee', 'Top Match 1', 'Top Match 2', 'Top Match 3']
recommendation_df.to_csv('Mentor_Mentee_Recommendations.csv', index=False)

print("Mentor-mentee recommendations have been generated and saved to 'Mentor_Mentee_Recommendations.csv'.")