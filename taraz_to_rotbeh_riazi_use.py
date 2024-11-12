import joblib

# بارگذاری مدل ذخیره‌شده
model_filename = 'konkoor_rank_predictor_model_riazi.pkl'
model = joblib.load(model_filename)

# تابع پیش‌بینی رتبه با توجه به تراز و منطقه
def predict_rank(teraz, region):
    return model.predict([[teraz, region]])[0]

# مثال: پیش‌بینی رتبه برای تراز 9500 و منطقه 2
predicted_rank = predict_rank(12000, 2)
print(f"Predicted Rank: {predicted_rank}")