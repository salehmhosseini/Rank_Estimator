import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib

# داده‌های ورودی
data = {
    'Teraz': [12000, 11500, 11000, 10000, 9000, 8000, 7000, 6000, 5000, 4000],
    'Region1': [21, 47, 98, 775, 3369, 9311, 18982, 33662, 55261, 76963],
    'Region2': [19, 56, 141, 991, 4897, 14562, 32313, 61327, 106965, 155583],
    'Region3': [5, 18, 35, 382, 2627, 9532, 24956, 54729, 107019, 168331],
    'Quota5%': [4, 14, 21, 147, 915, 3134, 7433, 14514, 25997, 37559],
    'Quota25%': [1, 1, 1, 11, 64, 258, 801, 1934, 4823, 8828]
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
model_filename = 'konkoor_rank_predictor_model_tajrobi.pkl'
joblib.dump(model, model_filename)
print(f"Model saved to {model_filename}")