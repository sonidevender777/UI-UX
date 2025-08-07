import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# === EXTRACT ===
print("📤 Extracting data...")
df = pd.read_csv("directory_style_customer_data.csv")
print("Initial shape:", df.shape)

# Drop unnecessary columns
df = df.drop(columns=["CustomerID", "FirstName", "LastName", "Email", "Phone", "JoinDate", "LastLogin"])

# Separate features and target
X = df.drop("Churned", axis=1)
y = df["Churned"]

# Identify column types
numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = X.select_dtypes(include=["object"]).columns

# === TRANSFORM ===
# Pipeline for numeric columns
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])
X[numeric_cols] = numeric_pipeline.fit_transform(X[numeric_cols])

# Encode categorical columns using LabelEncoder
for col in categorical_cols:
    X[col] = X[col].fillna(X[col].mode()[0])  # fill missing
    X[col] = LabelEncoder().fit_transform(X[col])

# Combine features and target
processed_df = pd.concat([X, y], axis=1)

# === LOAD ===
processed_df.to_csv("processed_customer_data.csv", index=False)
print("✅ ETL complete. File saved as 'processed_customer_data.csv'")
