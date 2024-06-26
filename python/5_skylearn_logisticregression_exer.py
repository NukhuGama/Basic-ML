# -*- coding: utf-8 -*-
# """5. SkyLearn-LogisticRegression_Exer

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/1746aJ_qel6MG0aSK-WvkinOw_vZ3mTMh

# Dataset untuk latihan bisa Anda unduh pada tautan [tautan](https://www.kaggle.com/dragonheir/logistic-regression). Seperti biasa, unggah dataset Social_Network_Ads pada session storage Google Colab.

# Setelah kita mengunggah berkas data pada Colab kita akan mengubah dataset menjadi dataframe Pandas. Jangan lupa untuk mengimpor library dasar dan menyesuaikan path/lokasi datanya ya.
# """

import pandas as pd

#membaca dataset dan emngubahnya menjadi dataframe
df = pd.read_csv('Social_Network_Ads.csv')
# df

# """#####Pada cell selanjutnya gunakan fungsi head() pada dataframe untuk melihat 10 baris pertama dari dataset."""

df.head()

# """#####Kita juga perlu melihat apakah ada nilai yang kosong pada setiap atribut dengan menggunakan fungsi info(). Dapat dilihat bahwa nilai pada semua kolom sudah lengkap.


# """

df.info()

# """#####Pada dataset terdapat kolom ‘User ID’. Kolom tersebut merupakan atribut yang tidak penting untuk dipelajari oleh model sehingga perlu dihilangkan. Untuk menghilangkan kolom dari dataframe, gunakan fungsi drop. Jangan lupa panggil fungsi get_dummies() untuk melakukan proses One-Hot Encoding karena label pada dataset kita merupakan data kategorikal."""

# drop kolom yang tidak diperlukan

data = df.drop(columns=['User ID'])

#jalankan proses one-hot encoding dengan pd.get_dummies

data = pd.get_dummies(data, dtype="int")
data

# """#####Kemudian kita pisahkan antara atribut dan label."""

#pisahkan atribut dan label
predictions = ['Age', 'EstimatedSalary', 'Purchased', 'Gender_Female', 'Gender_Male']

X = data[predictions]

y = data['Purchased']

# """#####Sebelum kita membagi data menjadi train dan test set, kita perlu melakukan standardisasi data seperti yang sudah dijelaskan di modul sebelumnya"""

#lakukan normalisasi terhadap data yang kita miliki
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
scaled_data = scaler.transform(X)
scaled_data = pd.DataFrame(scaled_data, columns=X.columns)
scaled_data.head()

# """#####Sekarang, kita akan membagi data menjadi train dan test set dengan fungsi train_test_split yang disediakan SKLearn."""

from sklearn.model_selection import train_test_split

#bagi data menjadi train dan test untuk setiap atribut dan label
X_train, X_test, y_train, y_test = train_test_split(scaled_data, y, test_size=0.2, random_state=1)

# """#####Setelah membagi data, kita buat model dengan membuat sebuah objek logistic regression. Setelah model dibuat, kita bisa melatih model kita dengan train set menggunakan fungsi fit().


# """

from sklearn import linear_model

#latih model dengan fungsi fit
model = linear_model.LogisticRegression()
model.fit(X_train, y_train)

# """#####Setelah model dilatih, kita bisa menguji akurasi model pada test set dengan memanggil fungsi score() pada objek model."""

# uji akurasi model
model.score(X_test, y_test)