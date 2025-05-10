import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

# Load data
df = pd.read_csv("train_data.csv")

# Convert genre strings to list
df["Genre_List"] = df["Genre_List"].apply(lambda x: x.strip("[]").replace("'", "").split(", "))

# Binarize labels
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(df["Genre_List"])

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["Cleaned_Summary"])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = OneVsRestClassifier(LogisticRegression(solver="liblinear"))
model.fit(X_train, y_train)

# Save all
joblib.dump(model, "genre_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(mlb, "label_binarizer.pkl")

print("Model training and saving completed.")
