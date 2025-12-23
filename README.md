# Super_Messy_Data_Cleaned
# Super Messy E-Commerce Data Cleaning Project

## Project Overview
This project focuses on cleaning and preparing a **highly messy e-commerce dataset** using **Python, Pandas, and NumPy**.  
The dataset contains missing values, inconsistent formats, duplicates, invalid entries, and outliers.

The goal is to transform raw, unreliable data into a **clean, analysis-ready dataset** suitable for EDA and machine learning tasks.

---

## Dataset Description
**Input File:**  
- `super_messy_ecommerce_test.csv`

**Output File:**  
- `Cleaned_Messy_data.csv`

### Key Columns:
- `ORDER_ID`
- `CUSTOMER_NAME`
- `AGE`
- `GENDER`
- `CITY`
- `ORDER_AMOUNT`
- `PAYMENT_METHOD`
- `ORDER_DATE`
- `DELIVERY_DAYS`

---

## Data Cleaning Steps Performed

### 1. Data Understanding
- Checked shape, data types, missing values, and summary statistics
- Identified duplicates and inconsistent column names

### 2. Column Standardization
- Converted column names to **UPPER_SNAKE_CASE**
- Fixed malformed column names

### 3. Missing & Invalid Values Handling
- Removed rows with missing `ORDER_ID`
- Filled missing:
  - `CUSTOMER_NAME` → `"Unknown"`
  - `AGE` → median value
  - `ORDER_AMOUNT` → median value
  - `DELIVERY_DAYS` → mean value
  - `ORDER_DATE` → median date

### 4. Data Type Fixes
- Converted numeric columns using `pd.to_numeric()`
- Converted date column using `pd.to_datetime()`
- Removed negative values using absolute transformation

### 5. Categorical Data Cleaning
- Standardized values for:
  - `GENDER` (Male, Female, Unspecified)
  - `PAYMENT_METHOD` (Cash, Card, UPI, Net_Banking)
- Cleaned inconsistent city names

### 6. Outlier Treatment
- Filtered age range between **18 and 70**
- Removed extreme `ORDER_AMOUNT` outliers using statistical thresholds

---

## Feature Engineering
New features created to enhance analysis:
- **ORDER_RANGE** → `low` / `high` (based on order amount)
- **DELIVERY_SPEED** → `fast` / `slow` (based on delivery days)

---

## Insights Derived
- Top cities by order count identified
- Average order amount calculated
- Most common payment method analyzed
- Delivery speed distribution evaluated

---

## Tools & Libraries Used
- **Python**
- **Pandas**
- **NumPy**

---

## How to Run the Project

```bash
pip install pandas numpy
python Supper_messy_Cleaned.py

