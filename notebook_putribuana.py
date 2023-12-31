# -*- coding: utf-8 -*-
"""notebook-putribuana

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10yWQ4zsTWidrRmwzm4ZKVN72LNHBaOIu

# Proyek Analisis Data: Bike-sharing-dataset
- Nama: Andi Engku Putribuana
- Email: andiengku1922@gmail.com
- Id Dicoding: putribuana

## Menentukan Pertanyaan Bisnis

- Bagaimana cuaca dapat mempengaruhi pengguna bike sharing?

- Apakah musim dapat berpengaruh terhadap pengguna bike sharing?

## Menyiapkan semua library yang dibuthkan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""## Data Wrangling

### Gathering Data
"""

# Membaca file CSV dari URL github dengan library pandas
day_df = pd.read_csv("https://raw.githubusercontent.com/putribuana/Dicoding-ProyekAkhirAnalisisData/main/BIke-sharing-datasets/day.csv")

# Menampilkan data day di beberapa baris data pertama
day_df.head()

"""tabel hour_df"""

# Membaca file CSV dari URL github dengan library pandas
hour_df = pd.read_csv("https://raw.githubusercontent.com/putribuana/Dicoding-ProyekAkhirAnalisisData/main/BIke-sharing-datasets/day.csv")

# Menampilkan data hour di beberapa baris data pertama
hour_df.head()

"""### Assessing Data

####**menilai tabel day_df**

method info() untuk memastikan tipe data di tabel day_df
"""

day_df.info()

"""Dari apa yang terlihat pada tabel day_df, terdapat kesalahan dalam jenis data pada kolom dteday yang semestinya merupakan datetime, bukan objek."""

#cek duplikasi
print("Jumlah duplikasi: ",day_df.duplicated().sum())
day_df.describe()

"""jika diperhatikan tidak terdapat duplikasi dan keanehan nilai pada day_df

**mengecek missing value**
"""

day_df.isna().sum()

"""berdasarkan pengecekan, data day_df tidak terdapat missing value

**Menilai parameter statistik**
"""

day_df.describe()

"""dari pengamtan penilaian parameter statistik, tidak terdapat parameter statistik yang tidak sesuai pada tabel day_df

####**menilai tabel hour_df**

memastikan tipe data hour_df
"""

hour_df.info()

"""pada tabel hour_df menunjukkan adanya kesalahan tipe data pada kolom dteday yang seharusnya berupa datetime, namun saat ini berbentuk objek."""

#cek duplikasi
print("Jumlah duplikasi: ",day_df.duplicated().sum())
day_df.describe()

"""tidak terdapat duplikasi pada data hour_df"""

#cek missing value
hour_df.isna().sum()

"""tidak terdapat missing value pada tabel hour_df"""

#mengecek parameter statistik
hour_df.describe()

"""dari pengamtan penilaian parameter statistik, tidak terdapat parameter statistik yang tidak sesuai pada tabel hour_df

####Rangkuman masalah pada data day_df dan hour_df adalah sebagai berikut :

1) pada tabel day_df, tipe data pada kolom dteday harusnya "datetime" bukan object

2) pada tabel hour_df, tipe data pada kolom dteday harusnya "datetime" bukan object

### Cleaning Data

Membersihkan data tabel day_df (berdasarkan masalah diatas, kita perlu memperbaiki tipe data yang salah)
"""

# mengganti tipe data di kolom dtday menjadi "datetime"
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

#cek data
day_df.info()

"""Membersihkan data tabel hour_df (berdasarkan masalah diatas, kita perlu memperbaiki tipe data yang salah)"""

# mengganti tipe data di kolom dtday menjadi "datetime"
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

#cek data
hour_df.info()

"""## Exploratory Data Analysis (EDA)

### Explore data *day_df*
"""

day_df.describe(include="all")

"""Dari data diatas, dapat diketaui :

* Data pada kolom "season" memiliki 4 nilai unik yaitu musim semi, musim panas, musim gugur, musim dingin.

* Data pada kolom "yr" menunjukkan tahun 2011 dan tahun 2012.

* Selanjutnya, data pada kolom "mnth" menunjukkan nilai dari 1 hingga 12, yang diasumsikan sebagai bulan.

* Selain itu, terdapat kolom-kolom "holiday", "weekday", dan "workingday" yang merupakan variabel biner, menandakan apakah hari tersebut adalah hari libur, hari kerja, atau hari libur tetapi bukan akhir pekan.

* Pada data pada kolom "weathersit" memiliki 3 nilai unik, yang diasumsikan sebagai kondisi cuaca seperti cerah, berawan, dan hujan.


"""

day_df.loc[day_df["season"] == 1, "season"] = "Springer"
day_df.loc[day_df["season"] == 2, "season"] = "Summer"
day_df.loc[day_df["season"] == 3, "season"] = "Fall"
day_df.loc[day_df["season"] == 4, "season"] = "Winter"

day_df.season.value_counts().sort_index()

#Data pada kolom "yr" menunjukkan biner 0 dan 1 yang diasumsikan menjadi tahun 2011 dan tahun 2012
day_df.loc[day_df["yr"] == 0, "yr"] = "2011"
day_df.loc[day_df["yr"] == 1, "yr"] = "2012"

day_df.yr.value_counts().sort_index()

#kolom "mnth" menunjukkan nilai dari 1 hingga 12, yang diasumsikan sebagai bulan.
day_df.mnth.value_counts().sort_index()

#kolom-kolom "holiday", "weekday", dan "workingday"
#yang merupakan variabel biner, menandakan apakah hari
#tersebut adalah hari libur,
#hari kerja, atau hari libur tetapi bukan akhir pekan.
day_df.loc[day_df["holiday"] == 0, "holiday"] = "Holiday"
day_df.loc[day_df["holiday"] == 1, "holiday"] = "Not a Holiday"

day_df.holiday.value_counts().sort_index()

day_df.loc[day_df["weekday"] == 0, "weekday"] = "Sun"
day_df.loc[day_df["weekday"] == 1, "weekday"] = "Mon"
day_df.loc[day_df["weekday"] == 2, "weekday"] = "Tue"
day_df.loc[day_df["weekday"] == 3, "weekday"] = "Wed"
day_df.loc[day_df["weekday"] == 4, "weekday"] = "Thu"
day_df.loc[day_df["weekday"] == 5, "weekday"] = "Fri"
day_df.loc[day_df["weekday"] == 6, "weekday"] = "Sat"

day_df.weekday.value_counts().sort_index()

day_df.loc[day_df["workingday"] == 0, "workingday"] = "Holiday"
day_df.loc[day_df["workingday"] == 1, "workingday"] = "Working Day"

day_df.workingday.value_counts().sort_index()

day_df.loc[day_df["weathersit"] == 1, "weathersit"] = "Clear"
day_df.loc[day_df["weathersit"] == 2, "weathersit"] = "Mist + Cloudy"
day_df.loc[day_df["weathersit"] == 3, "weathersit"] = "Light Snow"
day_df.loc[day_df["weathersit"] == 4, "weathersit"] = "Heavy Rain"

day_df.weathersit.value_counts().sort_index()

"""### Explore data *hour_df*"""

hour_df.describe(include="all")

"""Dari data diatas, dapat ditemukan bahwa :

* Top: Nilai yang paling sering muncul dalam setiap kolom. Contohnya, nilai yang paling sering muncul pada kolom "dteday" adalah "2011-01-01 00:00:00".

* Freq : Frekuensi kemunculan dari nilai yang paling sering muncul dalam setiap kolom. Contohnya, nilai "2011-01-01 00:00:00" pada kolom "dteday" muncul 1 kali.

* Mean : Rata-rata nilai dalam setiap kolom numerik. Contohnya, rata-rata dari kolom "yr" adalah 0.500684, yang kemungkinan mengindikasikan bahwa sekitar setengah dari data merujuk ke tahun 2011 dan setengahnya lagi ke tahun 2012.

* Std : Standar deviasi dari nilai dalam setiap kolom numerik. Standar deviasi mengukur seberapa tersebar atau tersebar data dari rata-rata. Semakin tinggi nilai standar deviasi, semakin besar variasi data dari rata-rata.

* "25%", "50%", "75%": Kuartil pertama, kuartil kedua (median), dan kuartil ketiga dari setiap kolom numerik. Kuartil pertama (25%) adalah nilai yang membagi data menjadi 25% terbawah, kuartil kedua (50%) adalah median yang membagi data menjadi 50% terbawah dan 50% teratas, dan kuartil ketiga (75%) membagi data menjadi 75% terbawah dan 25% teratas.
"""

hour_df.loc[hour_df["weathersit"] == 1, "weathersit"] = "Clear"
hour_df.loc[hour_df["weathersit"] == 2, "weathersit"] = "Mist + Cloudy"
hour_df.loc[hour_df["weathersit"] == 3, "weathersit"] = "Light Snow"
hour_df.loc[hour_df["weathersit"] == 4, "weathersit"] = "Heavy Rain"

hour_df.weathersit.value_counts().sort_index()

"""## Visualization & Explanatory Analysis

### Bagaimana cuaca dapat mempengaruhi pengguna bike sharing?
"""

byweathersit_df = day_df.groupby(by="weathersit").instant.nunique().reset_index()
byweathersit_df.rename(columns={
    "instant": "sum"
}, inplace=True)
byweathersit_df

plt.figure(figsize=(8, 4))

# Data dan visualisasi
data = byweathersit_df.sort_values(by="weathersit", ascending=False)
sns.barplot(
    y="sum",
    x="weathersit",
    data=data,
    color="darkblue",
)

plt.title("Pengaruh cuaca terhadap pengguna Bike Sharing", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=12)
plt.show()

"""### Apakah musim dapat berpengaruh terhadap pengguna bike sharing?"""

byseason_df = day_df.groupby(by="season").instant.nunique().reset_index()
byseason_df.rename(columns={
    "instant": "sum"
}, inplace=True)
byseason_df

plt.figure(figsize=(8, 4))

sns.barplot(
    y="sum",
    x="season",
    data=byseason_df.sort_values(by="season", ascending=False),
)
plt.title("Penggunaan Bike Sharing Berdasarkan Musim", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=12)
plt.show()

"""## Conclusion

####Kesimpulan pertanyaan 1
* Grafik batang diatas menunjukkan bahwa penggunaan bike sharing cenderung berkurang pada kondisi cuaca yang lebih buruk (nilai weathersit lebih tinggi). Disisi lain, penggunaan bike sharing cenderung lebih tinggi saat cuaca lebih cerah dan berkurang saat cuaca lebih buruk atau berawan.

####Kesimpulan pertanyaan 2
* Grafik batang diatas menunjukkan bahwa penggunaan bike sharing memiliki variasi yang signifikan terhadap musim yang berbeda. Dengan kata lain, penggunaan bike sharing cenderung lebih tinggi saat musim-musim yang lebih hangat seperti musim semi dan musim panas, dan cenderung menurun selama musim-musim yang lebih dingin seperti musim gugur dan musim dingin.

##Ekspor Dataset
"""

day_df.to_csv("day_data.csv", index=False)