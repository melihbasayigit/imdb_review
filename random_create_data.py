import random
import csv

# Veri sayısı
num_data = 10000

# CSV dosyasının adı
csv_file = "random_veri.csv"

# Verileri saklamak için boş bir liste oluşturun
data = []

# 1000 adet veri oluşturun
for _ in range(num_data):
    # Değişkenlerin değerlerini rastgele oluşturun
    x1 = random.uniform(0, 0.25)
    x2 = random.uniform(0, 0.25)
    x3 = random.uniform(0, 0.25)
    x4 = random.uniform(0, 0.25)
    # Toplamı hesaplayın
    y = x1 + x2 + x3 + x4

    # Verileri liste olarak saklayın
    data.append([x1, x2, x3, x4, y])

# CSV dosyasına yazma
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Başlık satırını yazın
    writer.writerow(["x1", "x2", "x3", "x4", "y"])
    # Verileri yazın
    writer.writerows(data)

print("Veriler başarıyla", csv_file, "dosyasına yazıldı.")


