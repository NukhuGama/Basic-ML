# -*- coding: utf-8 -*-
# """7. SkyLearn-PCA_Exer

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/14PtixtlWEBhYiTWUcWa-7QIT5SRt-LNu

# #**Latihan SKLearn PCA**

# #**Tujuan**
# ######Pada latihan ini, kita akan berlatih mengimplementasi PCA dengan library SKLearn.

# #**Tahapan Latihan**
# #####Tahapan pada latihan ini sebagai berikut:


# * Bagi dataset.
# * Latih model tanpa PCA.
# * Latih model dengan PCA.
# * Evaluasi hasil kedua model.

# #**Codelab**
# #####Pada Colaboratory impor library yang dibutuhkan.  Kemudian kita masukkan dataset iris dan bagi data menjadi train set dan test set.
# """

from sklearn import datasets
from sklearn.model_selection import train_test_split

#Pada Latihan ini kita menggunakan iris dataset
iris = datasets.load_iris()
atribut = iris.data
label = iris.target

#Bagi dataset manjasi train set dan test set
X_train, X_test, y_train, y_test = train_test_split(
    atribut, label, test_size=0.2, random_state=1
)

# """#####Kita akan menggunakan model Decision Tree dan menghitung berapa akurasinya tanpa menggunakan PCA. Akurasi tanpa PCA adalah 0.9666. Akurasi dari model Anda mungkin berbeda dengan keluaran di bawah."""

from sklearn import tree

decision_tree = tree.DecisionTreeClassifier()
first_model = decision_tree.fit(X_train, y_train)
first_model.score(X_test, y_test)

# """#####Kemudian kita akan menggunakan PCA dan menghitung variance dari setiap atribut. Hasilnya adalah 1 atribut memiliki variance sebesar 0.922, yang berarti atribut tersebut menyimpan informasi yang tinggi dan jauh lebih signifikan dari atribut lain."""

from sklearn.decomposition import PCA

#membuat objek PCA dengan 4 principal component
pca = PCA(n_components=4)

#mengaplikasikan PCA pada dataset
pca_attributes = pca.fit_transform(X_train)

# melihat variance dari setiap atribut
pca.explained_variance_ratio_

# """#####Melihat dari variance sebelumnya kita bisa mengambil 2 principal component terbaik karena total variance nya adalah 0.976 yang sudah cukup tinggi.

# """

# PCA dengan 2 principal component

pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.fit_transform(X_test)

# """######Kita akan menguji akurasi dari classifier setelah menggunakan PCA."""

# uji akurasi classifier
model2 = decision_tree.fit(X_train_pca, y_train)
print("Hasil pengujian akurasi setelah menggunakan PCA menjadi seperti di bawah ini:")
model2.score(X_test_pca, y_test)

# """#####Dari percobaan di atas bisa kita lihat bahwa dengan hanya 2 principal component atau 2 atribut saja model masih memiliki akurasi yang tinggi. Dengan principal component kamu bisa mengurangi atribut yang kurang signifikan dalam prediksi dan mempercepat waktu pelatihan sebuah model machine learning."""