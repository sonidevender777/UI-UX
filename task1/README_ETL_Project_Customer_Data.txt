
PROJECT: Data Pipeline Development (ETL)

TOOLS USED:
- pandas
- scikit-learn
  - Pipeline
  - SimpleImputer
  - LabelEncoder
  - StandardScaler

STEPS PERFORMED:
1. Extracted raw customer data from 'directory_style_customer_data.csv'.
2. Dropped irrelevant columns:
   - CustomerID
   - FirstName
   - LastName
   - Email
   - Phone
   - JoinDate
   - LastLogin
3. Applied preprocessing:
   - Filled missing numeric values with column mean.
   - Scaled numeric features using StandardScaler.
   - Filled missing categorical values with mode.
   - Encoded categorical values using LabelEncoder.
4. Combined transformed features and target column 'Churned'.
5. Saved clean data to 'processed_directory_customer_data.csv'.

USAGE:
- Place 'directory_style_customer_data.csv' in the same folder as the script.
- Run the script using:

    python etl_pipeline.py

- Output file 'processed_directory_customer_data.csv' will be saved in the same folder.
