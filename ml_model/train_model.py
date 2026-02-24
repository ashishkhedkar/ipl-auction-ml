import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("Data/combined_auction_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

print("Dataset Loaded Successfully")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

# Drop rows with missing values (ONLY for correct columns)
df = df.dropna(subset=["Base Price", "Winning Bid"])

# Features and Target
X = df[["Base Price"]]
y = df["Winning Bid"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)

print("\nModel Trained Successfully ")
print("Mean Absolute Error:", mae)