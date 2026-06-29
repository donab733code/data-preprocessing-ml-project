import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# ---------------------------------
# 1. Import Dataset and Explore
# ---------------------------------

df = pd.read_csv("HousingData.csv")   # Replace with your CSV file name

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

# ---------------------------------
# 2. Handle Missing Values
# ---------------------------------

# Select numerical columns
num_cols = df.select_dtypes(include=np.number).columns

# Fill missing values with mean
imputer = SimpleImputer(strategy='mean')
df[num_cols] = imputer.fit_transform(df[num_cols])

print("\nMissing Values After Imputation:")
print(df.isnull().sum())

# ---------------------------------
# 3. Categorical Encoding
# ---------------------------------

cat_cols = df.select_dtypes(exclude=np.number).columns

if len(cat_cols) > 0:
    from sklearn.preprocessing import LabelEncoder

    encoder = LabelEncoder()

    for col in cat_cols:
        df[col] = encoder.fit_transform(df[col])

    print("\nCategorical columns encoded successfully.")
else:
    print("\nNo categorical columns found. Encoding not required.")

# ---------------------------------
# 4. Standardize Numerical Features
# ---------------------------------

scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("\nFirst 5 rows after Standardization:")
print(df.head())

# ---------------------------------
# 5. Visualize Outliers
# ---------------------------------

plt.figure(figsize=(14,6))
sns.boxplot(data=df[num_cols])
plt.xticks(rotation=45)
plt.title("Boxplot Before Removing Outliers")
plt.show()

# ---------------------------------
# Remove Outliers using IQR
# ---------------------------------

Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1

df_clean = df[~((df[num_cols] < (Q1 - 1.5 * IQR)) |
                (df[num_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]

print("\nOriginal Dataset Shape :", df.shape)
print("Dataset Shape After Removing Outliers :", df_clean.shape)

# ---------------------------------
# Boxplot After Removing Outliers
# ---------------------------------

plt.figure(figsize=(14,6))
sns.boxplot(data=df_clean[num_cols])
plt.xticks(rotation=45)
plt.title("Boxplot After Removing Outliers")
plt.show()

print("\nData Preprocessing Completed Successfully!")

df_clean_raw = df[~((df[num_cols] < (Q1 - 1.5 * IQR)) |
                    (df[num_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]

df_clean_raw.to_csv("preprocessed_data.csv", index=False)