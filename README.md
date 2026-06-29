# Data Preprocessing - Boston Housing Dataset

## 📌 Project Overview
This project demonstrates end-to-end data preprocessing on the Boston Housing dataset using Python. It includes handling missing values, feature scaling, and outlier removal.

---

## 📊 Dataset
- Boston Housing Dataset
- 506 rows, 14 columns
- Source: Provided CSV file

---

## ⚙️ Steps Performed

### 1. Data Exploration
- Checked shape, data types, and missing values

### 2. Missing Value Handling
- Imputed numerical missing values using **mean strategy**

### 3. Feature Scaling
- Applied **StandardScaler** for normalization

### 4. Outlier Detection
- Used **Boxplot visualization**
- Removed outliers using **IQR method**

---

## 📉 Results
- Original dataset: 506 rows  
- After cleaning: 257 rows  
- Dataset is now clean and ready for ML models  

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- VS Code

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py