import pandas as pd

# Define a function to determine MBTI type from answers
def determine_mbti(answers):
    # Define the thresholds for each MBTI dimension
    introvert_score = answers[0] + answers[1] + answers[2]
    extravert_score = answers[2] + answers[1] + answers[0]
    sensing_score = answers[3] + answers[4] + answers[5]
    intuition_score = answers[5] + answers[4] + answers[3]
    thinking_score = answers[6] + answers[7]
    feeling_score = answers[7] + answers[6]
    judging_score = answers[8] + answers[9]
    perceiving_score = answers[9] + answers[8]
    
    # Determine MBTI type
    mbti_type = ''
    mbti_type += 'I' if introvert_score > 12 else 'E'
    mbti_type += 'S' if sensing_score > 12 else 'N'
    mbti_type += 'T' if thinking_score < 8 else 'F'
    mbti_type += 'J' if judging_score < perceiving_score else 'P'
    
    return mbti_type

# Read the CSV file
df = pd.read_csv('models/Responses.csv')

# Define the relevant columns for MBTI calculation
columns = [
    'When working on a project; I prefer to',
    'In social situations; I tend to',
    'When faced with a problem; I usually',
    'When making decisions; I rely more on',
    'In conversations; I tend to focus on',
    'When planning for the future; I',
    'When evaluating a situation; I consider',
    'In conflicts; I tend to',
    'In my daily routine; I prefer',
    'When faced with a deadline; I',
    'In social situations; I tend to'
]

# Filter the DataFrame to only include the relevant columns
df_relevant = df[columns]

# Calculate MBTI type for each row and store in a new column
df['MBTI Type'] = df_relevant.apply(lambda row: determine_mbti(row.tolist()), axis=1)

# Write the updated DataFrame to a new CSV file
df.to_csv('Responses_with_MBTI.csv', index=False)

print("MBTI types have been added and saved to 'Responses_with_MBTI.csv'.")