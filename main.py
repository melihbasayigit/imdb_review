import os
import pandas as pd

# Klasör yolunu belirtin
klasor_yolu = 'dataset/2_reviews_per_movie_raw'

# Boş bir DataFrame oluşturun
birlesik_df = pd.DataFrame()

kaydetme_sutunlari = ['rating', 'title', 'review']

# Rating değeri null olanları içeren bir DataFrame oluşturun
rating_null_df = pd.DataFrame()

# Klasördeki tüm CSV dosyalarını işleyin
for dosya in os.listdir(klasor_yolu):
    if dosya.endswith('.csv'):
        dosya_yolu = os.path.join(klasor_yolu, dosya)
        # CSV dosyasını okuyun
        df = pd.read_csv(dosya_yolu)
        # Rating değeri null olan satırları filtreleyin
        rating_null_columns = df[df['rating'] == 'Null']
        # Rating değeri null olan satırları ayrı bir DataFrame'e ekleyin
        rating_null_df = pd.concat([rating_null_df, rating_null_columns])
        # Rating değeri null olan satırları orijinal DataFrame'den çıkarın
        df = df[df['rating'] != 'Null']
        # Birleşik DataFrame'e ekleyin
        birlesik_df = pd.concat([birlesik_df, df])

# Title'ın uzunluk istatistikleri
title_uzunluk_istatistikleri = birlesik_df['title'].str.len().describe()

# Review'ın uzunluk istatistikleri
review_uzunluk_istatistikleri = birlesik_df['review'].str.len().describe()

# Rating değeri 10 olan DataFrame'ini bir dosyaya kaydedin
rating_null_df.to_csv('rating_null.csv', index=False, columns=kaydetme_sutunlari)

# Diğer rating değerlerini içeren DataFrame'ini başka bir dosyaya kaydedin
birlesik_df.to_csv('rating_not_null.csv', index=False, columns=kaydetme_sutunlari)
