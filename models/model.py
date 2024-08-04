import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the data
df = pd.read_csv('models/Responses.csv')

# Define cognitive functions mapping
cognitive_functions = {
    "When working on a project; I prefer to": ("Te", "Ti"),
    "In social situations; I tend to": ("Fe", "Fi"),
    "When faced with a problem; I usually": ("Ti", "Te"),
    "When making decisions; I rely more on": ("Te", "Ni"),
    "In conversations; I tend to focus on": ("Se", "Ne"),
    "When planning for the future; I": ("Ni", "Se"),
    "When evaluating a situation; I consider": ("Te", "Fi"),
    "In conflicts; I tend to": ("Fe", "Ti"),
    "In my daily routine; I prefer": ("Si", "Ne"),
    "When faced with a deadline; I": ("Si", "Ne"),
    "In social situations; I tend to": ("Fe", "Ti")
}

# Function to calculate cognitive function scores
def calculate_cognitive_scores(row):
    scores = {cf: 0 for cf in set([cf for cf_pair in cognitive_functions.values() for cf in cf_pair])}
    for question, (pos, neg) in cognitive_functions.items():
        if row[question] >= 4:
            scores[pos] += row[question] - 3
        else:
            scores[neg] += 4 - row[question]
    return pd.Series(scores)

# Apply the function to calculate cognitive function scores
cognitive_scores_df = df.apply(calculate_cognitive_scores, axis=1)

# Define MBTI type based on cognitive functions
def determine_mbti(row):
    # Dominant and Auxiliary functions for each MBTI type
    mbti_types = {
        "ISTJ": {"dominant": "Si", "auxiliary": "Te"},
        "ISFJ": {"dominant": "Si", "auxiliary": "Fe"},
        "INFJ": {"dominant": "Ni", "auxiliary": "Fe"},
        "INTJ": {"dominant": "Ni", "auxiliary": "Te"},
        "ISTP": {"dominant": "Ti", "auxiliary": "Se"},
        "ISFP": {"dominant": "Fi", "auxiliary": "Se"},
        "INFP": {"dominant": "Fi", "auxiliary": "Ne"},
        "INTP": {"dominant": "Ti", "auxiliary": "Ne"},
        "ESTP": {"dominant": "Se", "auxiliary": "Ti"},
        "ESFP": {"dominant": "Se", "auxiliary": "Fi"},
        "ENFP": {"dominant": "Ne", "auxiliary": "Fi"},
        "ENTP": {"dominant": "Ne", "auxiliary": "Ti"},
        "ESTJ": {"dominant": "Te", "auxiliary": "Si"},
        "ESFJ": {"dominant": "Fe", "auxiliary": "Si"},
        "ENFJ": {"dominant": "Fe", "auxiliary": "Ni"},
        "ENTJ": {"dominant": "Te", "auxiliary": "Ni"}
    }
    
    scores = row.dropna().to_dict()
    max_mbti = None
    max_score = -float('inf')
    
    for mbti, functions in mbti_types.items():
        try:
            dominant = functions["dominant"]
            auxiliary = functions["auxiliary"]
        except KeyError as e:
            print(f"KeyError: {e} in MBTI type: {mbti}")
            continue
        
        score = scores.get(dominant, 0) * 2 + scores.get(auxiliary, 0)
        
        if score > max_score:
            max_score = score
            max_mbti = mbti
    
    return max_mbti

# Calculate MBTI type for each student
df["MBTI"] = cognitive_scores_df.apply(determine_mbti, axis=1)

# Prepare data for the model
X = cognitive_scores_df
y = df["MBTI"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'mbti_classifier_model.pkl')

# Save the results to a new CSV file
df.to_csv('MBTI_Results.csv', index=False)