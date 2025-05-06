import pandas as pd
import pickle

# 1. Load Model Pipeline yang telah di-save
with open('model.pkl', 'rb') as model_file:
    pipeline = pickle.load(model_file)

# 2. Load Data Test
df_test = pd.read_csv('employee_test.csv')

def create_features(df):
    """Replikasi feature engineering yang sama seperti saat training"""
    features = df[[
        'TotalWorkingYears', 'Age', 'JobLevel', 'JobSatisfaction', 'JobRole','MonthlyIncome',
        'YearsInCurrentRole', 'OverTime', 'BusinessTravel',
        'MaritalStatus', 'WorkLifeBalance','EnvironmentSatisfaction', 'EducationField',
        'YearsAtCompany', 'YearsSinceLastPromotion'
    ]].copy()
    
    features['IncomePerLevel'] = features['MonthlyIncome'] / features['JobLevel'].replace(0, 1)
    features['PromotionFrequency'] = features['YearsAtCompany'] / (features['YearsSinceLastPromotion'].replace(0, 0.1))  # Avoid zero division
    features['TenureRatio'] = features['TotalWorkingYears'] / (features['Age'] + 1e-2)
    
    return features

test_features = create_features(df_test)
predictions = pipeline.predict(test_features)

value_counts = pd.Series(predictions).value_counts()
print("Distribusi Prediksi Attrition:");
print(value_counts)