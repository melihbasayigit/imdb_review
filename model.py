import pandas as pd
import random

seed_value = 3131
rating_amount = 280

# CSV dosyasını oku
df = pd.read_csv('rating_not_null.csv')

# Karıştırma için seed ayarla
random.seed(seed_value)

# Verileri karıştır
df_shuffled = df.sample(frac=1, random_state=seed_value).reset_index(drop=True)

# print("İlk 100 veri:")
# print(df_shuffled.head(100))

# print("\nSon 100 veri:")
# print(df_shuffled.tail(100))

sampled_indices = []
for rating in range(1, 11):
    indices = df_shuffled.index[df_shuffled['rating'] == rating].tolist()
    sampled_indices.extend(indices[:rating_amount])

sampled_df = df_shuffled.iloc[sampled_indices].reset_index(drop=True)

sampled_df_shuffled = sampled_df.sample(frac=1, random_state=seed_value).reset_index(drop=True)

print(sampled_df_shuffled)

print(sampled_df_shuffled['rating'].value_counts())

print("Toplam satır sayısı:", df.shape[0])
