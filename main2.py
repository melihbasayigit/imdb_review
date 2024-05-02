import os
import pandas as pd

# Klasör yolunu belirtin
klasor_yolu = 'dataset/2_reviews_per_movie_raw'

# Boş bir DataFrame oluşturun
birlesik_df = pd.DataFrame()

# Klasördeki tüm CSV dosyalarını işleyin
for dosya in os.listdir(klasor_yolu):
    if dosya.endswith('.csv'):
        dosya_yolu = os.path.join(klasor_yolu, dosya)
        # CSV dosyasını okuyun
        df = pd.read_csv(dosya_yolu)
        # Birleşik DataFrame'e ekleyin
        birlesik_df = pd.concat([birlesik_df, df])

# Rating için histogram
rating_histogram = birlesik_df['rating'].value_counts().sort_index()

# Title'ın uzunluk istatistikleri
title_uzunluk_istatistikleri = birlesik_df['title'].str.len().describe()

# Review'ın uzunluk istatistikleri
review_uzunluk_istatistikleri = birlesik_df['review'].str.len().describe()

print("Rating Histogramı:")
print(rating_histogram)
print("\nTitle Uzunluk İstatistikleri:")
print(title_uzunluk_istatistikleri)
print("\nReview Uzunluk İstatistikleri:")
print(review_uzunluk_istatistikleri)
