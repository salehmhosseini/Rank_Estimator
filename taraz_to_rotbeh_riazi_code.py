import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib

# داده‌های ورودی
data = {
    'Teraz': [12000, 11500, 11000, 10000, 9000, 8000, 7000, 6000, 5000, 4000],
    'Region1': [7 , 34 , 70 , 567 , 1824 , 4525 , 8901 , 18826 , 23757 , 36011],
    'Region2': [3 , 27 , 47 , 300 , 1026 , 2837 , 6608 , 17573 , 24067 , 38548],
    'Region3': [1 , 4 , 7 , 54 , 238 , 825 , 2492 , 8982 , 13673 , 24983],
    'Quota5%': [1 , 3 , 7 , 53 , 205 , 539 , 1145 , 2858 , 3891 , 6138],
    'Quota25%': [1 , 1 , 1 , 1 , 3, 16 , 69 , 308 , 507 , 917]
}

df = pd.DataFrame(data)

# تبدیل داده‌ها به فرمت طولانی برای مدل
df_melted = df.melt(id_vars=['Teraz'], var_name='Region', value_name='Rank')

# تبدیل نوع منطقه به عددی
region_mapping = {'Region1': 1, 'Region2': 2, 'Region3': 3, 'Quota5%': 4, 'Quota25%': 5}
df_melted['Region'] = df_melted['Region'].map(region_mapping)

# تقسیم داده‌ها به ورودی و خروجی
X = df_melted[['Teraz', 'Region']]
y = df_melted['Rank']

# تقسیم داده‌ها به مجموعه آموزش و تست
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# استفاده از مدل درخت تصمیم برای پیش‌بینی
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# ذخیره‌سازی مدل
model_filename = 'konkoor_rank_predictor_model_riazi.pkl'
joblib.dump(model, model_filename)
print(f"Model saved to {model_filename}")