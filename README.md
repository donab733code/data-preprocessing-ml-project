# 🏠 Housing Data Preprocessing Project
TASK 1

## 📌 Project Overview
This project focuses on **data cleaning and preprocessing** of a housing dataset.  
The objective is to transform raw data into a clean, structured, and machine-learning-ready format.

Data preprocessing is a critical step in any ML pipeline because it directly affects model accuracy, stability, and performance.

---

## 🎯 Objectives
- Import and explore dataset
- Handle missing values
- Encode categorical variables
- Detect and remove outliers
- Standardize numerical features
- Prepare final dataset for machine learning models

---

## 🛠️ Tools & Libraries Used
- Python 🐍
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📂 Dataset Information
The dataset used is `HousingData.csv`, which contains housing-related features such as:
- Numerical attributes (e.g., area, price-related factors)
- Categorical variables (if present)
- Target variable representing housing value

---

## 🔄 Data Preprocessing Workflow

### 1. Data Loading & Exploration
- Dataset loaded using Pandas
- Basic exploration using:
  - `.head()`
  - `.info()`
  - `.describe()`
- Checked data types and missing values

---

### 2. Handling Missing Values
- Identified missing values in numerical columns
- Applied **mean imputation** using `SimpleImputer`
- Ensured dataset completeness for further processing

---

### 3. Categorical Encoding
- Identified categorical features
- Converted categorical variables into numeric form using **Label Encoding**
- Ensured compatibility with ML algorithms

---

### 4. Outlier Detection & Removal
- Used **Interquartile Range (IQR) method**
- Visualized outliers using **Seaborn boxplots**
- Removed extreme values to improve data quality and model performance

---

### 5. Feature Scaling
- Applied **StandardScaler**
- Standardized numerical features:
  - Mean = 0
  - Standard Deviation = 1
- Improved performance for distance-based ML models

---

## 📊 Data Visualization
- Boxplots used for:
  - Detecting outliers before cleaning
  - Verifying data distribution after cleaning

---

## 📁 Output
The final cleaned dataset is saved as:
