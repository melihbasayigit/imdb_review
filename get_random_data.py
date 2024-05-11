import csv
import random

import pandas as pd

# SECTION 1 : DOSYA OKUMA KODLARI

def readCSVFile():

    # CSV dosyasının adı
    csv_file = "random_veri.csv"

    # Verileri saklamak için boş bir liste oluşturun
    data = []

    # CSV dosyasını okuyun
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        # Başlık satırını atlayın
        next(reader)
        # Her satırı okuyun
        for row in reader:
            # Her satırı float'a dönüştürerek veri listesine ekleyin
            row = [float(value) for value in row]
            data.append(row)


# SECTION 2 : VERİ ANALİTİĞİ

def analyzeData():
    # Aralıkların alt sınırlarını tanımlayın
    interval_lower_bounds = [i / 10 for i in range(10)]

    # Aralıklar için sayaçları saklamak için bir sözlük oluşturun
    interval_counts = {}

    # Her bir aralık için sayaçları sıfırlayın
    for lower_bound in interval_lower_bounds:
        interval_counts[(lower_bound, lower_bound + 0.1)] = 0

    # Veri listesindeki her satırı kontrol edin
    for row in data:
        # Y değerini alın
        y_value = row[-1]  # Son sütun y değerlerini içerir
        # Y değeri hangi aralığa giriyor kontrol edin ve ilgili sayaçları artırın
        for lower_bound in interval_lower_bounds:
            if lower_bound <= y_value < lower_bound + 0.1:
                interval_counts[(lower_bound, lower_bound + 0.1)] += 1
                break  # Aralığı bulduğumuzda döngüyü sonlandırın

    # Sonuçları yazdırın
    for interval, count in interval_counts.items():
        print(f"{interval[0]:.1f} ile {interval[1]:.1f} arasında olan veri sayısı:", count)



# SECTION 3 : EN KÜÇÜK OLANA GÖRE LİMİTLEYİP EŞİT SAYIDA VERİ ALMAK
def limitAllDataWithMin():

    # En küçük sayıda veriyi içeren aralığı bulun
    min_count = min(interval_counts.values())

    # Her aralıktan en küçük sayıda veriyi alın
    selected_data = []
    for interval, count in interval_counts.items():
        selected_data.extend([row for row in data if interval[0] <= row[-1] < interval[0] + 0.1][:min_count])

    # Seçilen veri sayısını kontrol edin
    print("Her aralıktan en küçük sayıda seçilen veri sayısı:", len(selected_data))


    new_csv_file = "selected_veri.csv"

    # Yeni CSV dosyasına yazma
    with open(new_csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Başlık satırını yazın
        writer.writerow(["x1", "x2", "x3", "x4", "y"])
        # Verileri yazın
        writer.writerows(selected_data)


# SECTION 4 : SEED İLE SHUFFLE
def readWithSeed():
    # CSV dosyasını oku
    df = pd.read_csv("selected_veri.csv")

    # Veriyi rastgele karıştır
    seed_değeri = 3131
    random.seed(seed_değeri)
    df_shuffle = df.sample(frac=1,random_state=seed_değeri).reset_index(drop=True)

    # Karıştırılmış veriyi yazdır veya başka bir CSV dosyasına kaydet
    print(df_shuffle.head(10))
    print(df_shuffle.tail(10))
    # df_shuffle.to_csv("shuffled_selected_veri.csv", index=False)  # CSV dosyasına kaydetmek için

readWithSeed()