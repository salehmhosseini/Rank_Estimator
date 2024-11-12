import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib

# داده‌های ورودی
data = {
    'Teraz': [12000, 11500, 11000, 10000, 9000, 8000, 7000, 6000, 5000, 4000],
    'Region1': [3 , 5 , 30 , 212 , 951 , 2945 , 6429 , 12579 , 23433 , 36072],
    'Region2': [4 , 7 , 42 , 278 , 1289 , 4325 , 11259 , 27853 , 54797 , 85418],
    'Region3': [3 , 7 , 19 , 189         , 1193 , 5692 , 17966 , 49686 , 102204 , 164488],
    'Quota5%': [2 , 2 , 6 , 43 , 216 , 795 , 2262 , 5795 , 11608 , 18469],
    'Quota25%': [1 , 1 , 2, 4, 7, 37, 163 , 656 , 1730 , 3232]
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
model_filename = 'konkoor_rank_predictor_model_ensani.pkl'
joblib.dump(model, model_filename)
print(f"Model saved to {model_filename}")