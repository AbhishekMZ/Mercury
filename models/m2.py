import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, fcluster

# Load the dataset from CSV
df = pd.read_csv('models/Responses.csv')

# Strip leading and trailing spaces from column names
df.columns = df.columns.str.strip()

# Print column names to inspect
print(df.columns)

# Define the mapping of questions to cognitive functions
cognitive_functions_questions = {
    'Ti': ['When faced with a problem; I usually', 'When making decisions; I rely more on'],
    'Te': ['When faced with a deadline; I', 'In conflicts; I tend to'],
    'Fi': ['In conversations; I tend to focus on', 'In social situations; I tend to'],
    'Fe': ['In my daily routine; I prefer', 'Are you open to the idea of being a mentor?'],
    'Si': ['When evaluating a situation; I consider', 'In social situations; I tend to'],
    'Se': ['When working on a project; I prefer to', 'What type of hobbies are you primarily into?'],
    'Ni': ['When planning for the future; I', 'What is your field of study?'],
    'Ne': ['Would you like to have an academic mentor to help you with college?', 'How often would you like to communicate with your mentor?']
}

# Function to encode categorical data
def encode_categorical(df, questions):
    encoded_data = df[questions].apply(lambda col: col.astype('category').cat.codes)
    return encoded_data

# Function to score cognitive functions based on responses
def score_cognitive_function(df, questions):
    encoded_data = encode_categorical(df, questions)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(encoded_data)
    return scaled_data.mean(axis=1)

# Calculate scores for each cognitive function
function_scores = {function: score_cognitive_function(df, questions) for function, questions in cognitive_functions_questions.items()}

# Add function scores to dataframe
for function, scores in function_scores.items():
    df[function] = scores

# Define the MBTI types and their corresponding dominant and auxiliary functions
mbti_functions = {
    'INTJ': ['Ni', 'Te'],
    'ENTP': ['Ne', 'Ti'],
    'ISFJ': ['Si', 'Fe'],
    'ENFP': ['Ne', 'Fi'],
    'ISTJ': ['Si', 'Te'],
    'ESFP': ['Se', 'Fi'],
    'INFJ': ['Ni', 'Fe'],
    'ESTP': ['Se', 'Ti'],
    'INFP': ['Fi', 'Ne'],
    'ISTP': ['Ti', 'Se'],
    'ESTJ': ['Te', 'Si'],
    'ESFJ': ['Fe', 'Si'],
    'ENTJ': ['Te', 'Ni'],
    'ISFP': ['Fi', 'Se'],
    'INTP': ['Ti', 'Ne'],
    'ENFJ': ['Fe', 'Ni']
}

# Function to determine MBTI type based on dominant and auxiliary functions
def determine_mbti_type(row):
    # Find the dominant and auxiliary functions
    dominant_auxiliary = [(row[function], mbti_type) for mbti_type, functions in mbti_functions.items() for function in functions]
    dominant_auxiliary.sort(reverse=True)
    dominant_type = dominant_auxiliary[0][1]
    return dominant_type

# Determine MBTI type for each participant
df['MBTI Type'] = df.apply(determine_mbti_type, axis=1)

# Save the results to a new CSV file
df.to_csv('cognitive_functions_mbti.csv', index=False)

# Output the relevant columns
df[['Name', 'MBTI Type']]
