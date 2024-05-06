import pandas as pd
import random

seed_value = 78

# CSV dosyasını oku
df = pd.read_csv('rating_not_null.csv')

# Karıştırma için seed ayarla
random.seed(seed_value)

# Verileri karıştır
df_shuffled = df.sample(frac=1, random_state=random.seed())

print("İlk 100 veri:")
print(df.head(100))

print("\nSon 100 veri:")
print(df.tail(100))
