# import library pandas
import pandas as pd

data = pd.read_csv('shopping_data_missingvalue.csv')
print("Data Sebelum Pre-Processing : ")
print(data)

# Melihat jumlah missing value pada setiap kolom
missing_value = data.isnull().sum()
print("Jumlah missing values pada setiap kolom :")
print(missing_value)

# Menghapus baris data yang mengandung missing value
data_clean = data.dropna()
print ("Data setelah missing value dihilangkan : ")
print(data_clean)

# Mengisi nilai-nilai yang hilang dengan mean
data_mean = data.fillna(data.mean(numeric_only=True))
print("Data setelah missing value diisi dengan mean : ")
print(data_mean)

# Mengisi nilai-nilai missing value dengan median
data_median = data.fillna(data.median(numeric_only=True))
print("Data setelah missing value diisi dengan median : ")
print(data_median)