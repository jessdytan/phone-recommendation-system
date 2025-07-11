# -*- coding: utf-8 -*-
"""MLT_CellphoneRecommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OTVzDqmSQ0Rv7s5h7fqqVrafnki_t7gO

# **Proyek Sistem Rekomendasi : Rekomendasi Lagu menggunakan Content-Based Recommendation**

- Nama: Jessindy Tanuwijaya
- Email: tanjess676@gmail.com
- ID Dicoding: jessdytan

## 1. Import Library/Packages
"""

!pip install tensorflow_recommenders

# Sistem & File Handling
import os                         # Operasi sistem file & direktori
import shutil                     # Menyalin dan memindahkan file
import zipfile                    # Menangani file ZIP (ekstraksi, kompresi)
import io                         # Operasi I/O berbasis memori
from pathlib import Path          # Representasi path file & direktori modern

# Operasi Numerik & Data
import math                       # Fungsi matematika dasar
import numpy as np                # Operasi array, vektor, dan matriks
import pandas as pd               # Manipulasi dan analisis data tabular

# Visualisasi Data
import matplotlib.pyplot as plt   # Visualisasi dasar (plot, histogram, dll.)
import seaborn as sns             # Visualisasi statistik (heatmap, boxplot, dll.)

# Preprocessing
from sklearn.preprocessing import LabelEncoder  # Mengubah label kategorik jadi numerik
from sklearn.preprocessing import StandardScaler  # Standarisasi fitur (mean=0, std=1)
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_recommenders as tfrs


# Model Machine Learning
from sklearn.linear_model import LogisticRegression         # Model klasifikasi linier
from sklearn.neighbors import KNeighborsClassifier          # Algoritma K-NN
from sklearn.ensemble import RandomForestClassifier         # Random Forest (model ensambel)

# Evaluasi Model
from sklearn.metrics import (confusion_matrix,              # Matriks kebingungan
                             precision_score,               # Skor presisi
                             recall_score,                  # Skor recall
                             f1_score,                      # Skor F1
                             accuracy_score,                # Skor akurasi
                             classification_report)         # Laporan klasifikasi lengkap

# Split Data & Optimasi Model
from sklearn.model_selection import train_test_split        # Membagi data latih & uji
from sklearn.model_selection import cross_val_score         # Validasi silang
from sklearn.model_selection import KFold                   # K-Fold cross-validation
from sklearn.model_selection import GridSearchCV            # Pencarian grid hyperparameter
from sklearn.model_selection import RandomizedSearchCV      # Pencarian acak hyperparameter

# Scikit-learn Shortcut
import sklearn as sk                # Shortcut opsional untuk cek versi atau struktur

from sklearn.preprocessing import MinMaxScaler

"""## 2. Data Wrangling

### 2.1 Download and Extract Dataset From Kaggle

Langkah-langkah untuk Mendapatkan kaggle.json:
1. Login ke Kaggle:
  
  Pergi ke Kaggle dan login menggunakan akun kamu. Jika belum punya akun, Anda bisa mendaftar terlebih dahulu.

2. Buka Halaman Akun Anda:
  
  Setelah login, klik ikon profil di sudut kanan atas halaman, kemudian pilih "**My Account**" dari dropdown menu.

3. Scroll ke Bagian API:
  
  Di halaman "Account", scroll ke bawah sampai menemukan bagian yang bernama "API". Di bagian ini ada tombol "**Create New API Token**". Klik tombol tersebut untuk membuat token API baru.

4. Download kaggle.json:

  Setelah klik tombol "Create New API Token", file kaggle.json akan otomatis diunduh ke komputer Anda.File ini berisi dua informasi penting: username dan key, yang akan digunakan untuk mengakses Kaggle API.
"""

from google.colab import files, userdata
# upload kaggle.json
files.upload()

"""Kode di bawah bertujuan untuk menyiapkan kredensial API Kaggle dengan cara memindahkan file kaggle.json ke folder yang tepat di Google Colab, sehingga API Kaggle dapat digunakan untuk mengakses dataset atau model secara otomatis dan aman."""

# Buat folder .kaggle di home directory
os.makedirs('/root/.kaggle', exist_ok=True)

# Pindahkan kaggle.json ke folder tersebut
shutil.move('kaggle.json', '/root/.kaggle/kaggle.json')

# Ubah permission supaya hanya bisa dibaca oleh user
os.chmod('/root/.kaggle/kaggle.json', 600)

"""Setelah menjalankan perintah dibawah ini, file zip dataset akan diunduh ke direktori kerja saat ini di Google Colab. Anda dapat mengekstrak dan menggunakannya untuk proyek Anda."""

!kaggle datasets download -d meirnizri/cellphones-recommendations

"""Mengekstrak seluruh isi file zip ke dalam folder dataset. Folder ini akan dibuat secara otomatis jika belum ada."""

with zipfile.ZipFile("cellphones-recommendations.zip", 'r') as zip_ref:
    zip_ref.extractall("dataset")

"""### 2.2 Assessing Data

#### Membaca dan mengimpor dataset ponsel.
"""

phone = pd.read_csv('/content/dataset/cellphones data.csv')
rating = pd.read_csv('/content/dataset/cellphones ratings.csv')
user = pd.read_csv('/content/dataset/cellphones users.csv')

df_merge = rating.merge(phone, on="cellphone_id", how="left").merge(user, on="user_id", how="left")

"""#### Menampilkan 5 data teratas"""

phone.head()

rating.head()

user.head()

"""#### Menampilkan informasi gambaran umum dataset"""

phone.info()

rating.info()

user.info()

"""#### Mengetahui jumlah baris dan kolom"""

# Mengetahui berapa banyak baris dan kolom dalam dataframe phone
print("Banyak Baris dalam Cellphones Data:",phone.shape[0])
print("Banyak Kolom dalam Cellphones Data:", phone.shape[1])

# Mengetahui berapa banyak baris dan kolom dalam dataframe rating
print("\nBanyak Baris dalam Cellphones Ratings:",rating.shape[0])
print("Banyak Kolom dalam Cellphones Ratings:", rating.shape[1])

# Mengetahui berapa banyak baris dan kolom dalam dataframe user
print("\nBanyak Baris dalam Cellphones Users:",user.shape[0])
print("Banyak Kolom dalam Cellphones Users:", user.shape[1])

"""#### Menampilkan data statistik dataset"""

phone.describe()

rating.describe()

user.describe()

"""#### Mengecek duplikat dalam data"""

phone.duplicated().sum()

rating.duplicated().sum()

user.duplicated().sum()

"""Kesimpulan: Tidak ada data yang duplikat

#### Mengecek data hilang
"""

phone.isnull().sum()

rating.isnull().sum()

user.isnull().sum()

"""Terdapat 1 baris data yang hilang pada kolom occupation

## 3. Exploratory Data Analysis (EDA)

### 3.1 Distribusi Operation System
"""

plt.figure(figsize=(8, 6))
sns.countplot(x=phone['operating system'], data=phone)
plt.title('Distribusi OS')
plt.ylabel('Jumlah')
plt.show()

"""### 3.2 Rating ponsel"""

plt.figure(figsize=(8, 4))
sns.countplot(x='rating',hue='rating', data=df_merge, palette='viridis')
plt.title('Distribusi Rating Ponsel')
plt.xlabel('Rating')
plt.ylabel('Jumlah')
plt.show()

"""Terdapat Outlier pada rating, dari skala 1-10, ada rating 18

### 3.3 Ponsel Popular
"""

top_phones = df_merge['model'].value_counts().head(10)
sns.barplot(x=top_phones.values, y=top_phones.index,hue=top_phones.index, palette='viridis')
plt.title('10 Ponsel Paling Banyak Direview')
plt.xlabel('Jumlah Review')
plt.ylabel('Model')
plt.show()

"""### 3.4 Distribusi Pekerjaan dan Rating"""

occupation_rating = df_merge.groupby('occupation')['rating'].mean().sort_values(ascending=False)
occupation_rating.plot(kind='barh', figsize=(10, 15), color='skyblue')
plt.title('Rata-rata Rating per Pekerjaan')
plt.xlabel('Rata-rata Rating')
plt.ylabel('Pekerjaan')
plt.show()

"""Masih banyak data yang tidak konsisten untuk pekerjaan, seperti IT, team worker in it,it, healthare dan healthcare, dan sebagainya.

## 4. Data Preprocessing

Mengecek data yang hilang
"""

print(df_merge.isnull().sum())

"""Mendapatkan informasi dataframe"""

df_merge.info()

"""Ubah format release data menjadi datetime"""

df_merge['release date'] = pd.to_datetime(df_merge['release date'], dayfirst=True, errors='coerce')

"""Drop kolom yang memiliki missing values"""

df = df_merge.dropna(subset=['occupation'])

"""Ubah rating menjadi skala 1-10"""

df_merge = df_merge[df_merge['rating'] != 18]

"""Menyamakan nama pekerjaan agar konsisten"""

df_merge['occupation'] = df_merge['occupation'].str.lower()

#Mengubah value 'healthare' pada kolom "occupation" menjadi 'healthcare'
df_merge['occupation'] = df_merge['occupation'].replace('healthare', 'healthcare')

#Mengubah value 'it' pada kolom "occupation" menjadi 'information technology'
df_merge['occupation'] = df_merge['occupation'].replace('team worker in it', 'it')

"""## 5. Building Recommendation System Content-Based Filtering

Drop baris yang memiliki id ponsel duplikat
"""

df_clean = df_merge.drop_duplicates('cellphone_id')

"""Mengubah kolom-kolom yang dipilih sebagai fitur rekomendasi dari DataFrame df_clean menjadi list"""

cellphone_id = df_clean['cellphone_id'].tolist()
brand = df_clean['brand'].tolist()
model = df_clean['model'].tolist()
operating_system = df_clean['operating system'].tolist()
memory = df_clean['internal memory'].tolist()
ram = df_clean['RAM'].tolist()

print(len(cellphone_id))
print(len(brand))
print(len(model))
print(len(operating_system))
print(len(memory))
print(len(ram))

""" Membuat DataFrame baru bernama cellphone_new dari daftar (list) yang sebelumnya telah diekstrak dari df_clean."""

cellphone_new = pd.DataFrame({
    'id': cellphone_id,
    'brand': brand,
    'model': model,
    'os': operating_system,
    'memory': memory,
    'ram': ram
})
cellphone_new

"""Berikut adalah sample datanya:"""

data = cellphone_new
data.sample(5)

"""Mengubah teks pada kolom brand menjadi representasi numerik menggunakan TF-IDF (Term Frequency-Inverse Document Frequency). TF-IDF adalah tools untuk mengubah kumpulan teks menjadi vektor angka berdasarkan frekuensi kata yang disesuaikan dengan seberapa umum kata tersebut di seluruh dokumen."""

# Inisialisasi TfidfVectorizer
tfid = TfidfVectorizer()

# Melakukan perhitungan idf pada data brand
tfid.fit(data['brand'])

# Mapping array dari fitur index integer ke fitur brand
tfid.get_feature_names_out()

tfidf_matrix = tfid.fit_transform(data['brand'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

tfidf_matrix.todense()

"""Menampilkan hasil acak dari matriks TF-IDF dalam bentuk tabel agar lebih mudah dibaca"""

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tfid.get_feature_names_out(),
    index=data.model
).sample(10, axis=1).sample(10, axis=0)

""" Mengukur kemiripan antar teks dalam kolom brand berdasarkan representasi TF-IDF."""

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""Analisis kemiripan antar model handphone berdasarkan brand"""

cosine_sim_df = pd.DataFrame(cosine_sim, index=data['model'], columns=data['model'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Fungsi untuk memberikan rekomendasi model handphone yang mirip dengan model tertentu berdasarkan nilai cosine similarity."""

def model_recommendations(model, similarity_data=cosine_sim_df, items=data[['model','brand','os','memory','ram']], k=5):

    index = similarity_data.loc[:,model].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop model agar nama model yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(model, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

"""Uji coba sistem rekomendasi"""

model_recommendations('iPhone 13 Mini')

"""Evaluasi Model Rekomendasi"""

def precision_at_k(recommended_items, true_items, k):
    recommended_at_k = recommended_items[:k]
    relevant = set(recommended_at_k) & set(true_items)
    return len(relevant) / k

def recall_at_k(recommended_items, true_items, k):
    recommended_at_k = recommended_items[:k]
    relevant = set(recommended_at_k) & set(true_items)
    return len(relevant) / len(true_items) if true_items else 0

def f1_score_at_k(recommended_items, true_items, k):
    precision = precision_at_k(recommended_items, true_items, k)
    recall = recall_at_k(recommended_items, true_items, k)
    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)

def ndcg_at_k(recommended_items, true_items, k):
    dcg = 0.0
    for i, item in enumerate(recommended_items[:k]):
        rel = 1 if item in true_items else 0
        dcg += rel / np.log2(i + 2)

    # Ideal DCG (IDCG)
    ideal_rels = [1] * min(len(true_items), k)
    idcg = sum(rel / np.log2(i + 2) for i, rel in enumerate(ideal_rels))

    return dcg / idcg if idcg > 0 else 0

"""Ubah hasil rekomendasi menggunakan content-based filtering sebelumnya menjadi list"""

recommended_df = model_recommendations('iPhone 13 Mini', k=5)
recommended_items = recommended_df['model'].tolist()

"""Membuat Ground Truth (seperti data relevansi atau preferensi)"""

true_items = ['iPhone 13', 'iPhone 13 Pro', 'iPhone 12 Mini']  # relevan item

"""Menjalankan fungsi untuk menghitung metrik evaluasinya"""

print("Precision@5:", precision_at_k(recommended_items, true_items, 5))
print("Recall@5:", recall_at_k(recommended_items, true_items, 5))
print("F1 Score@5:", f1_score_at_k(recommended_items, true_items, 5))
print("NDCG@5:", ndcg_at_k(recommended_items, true_items, 5))

""" ## 6. Building Recommendation System Collaborative Filtering"""

df = rating
df

# Mengubah user_id menjadi list tanpa nilai yang sama
user_ids = df['user_id'].unique().tolist()
print('list user_id: ', user_ids)

# Melakukan encoding user_id
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded user_id : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke user_id
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke user_id: ', user_encoded_to_user)

# Mengubah cellphone_id menjadi list tanpa nilai yang sama
cellphone_ids = df['cellphone_id'].unique().tolist()

# Melakukan proses encoding cellphone_id
cellphone_to_cellphone_encoded = {x: i for i, x in enumerate(cellphone_ids)}

# Melakukan proses encoding angka ke cellphone_id
cellphone_encoded_to_cellphone = {i: x for i, x in enumerate(cellphone_ids)}

# Mapping ke df
df['user'] = df['user_id'].map(user_encoded_to_user)
df['cellphone'] = df['cellphone_id'].map(cellphone_to_cellphone_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah cellphone
num_cellphones = len(cellphone_encoded_to_cellphone)
print(num_cellphones)

# Mengubah rating menjadi nilai float
df['rating'] = df['rating'].values.astype(np.float32)

# Nilai minimum rating
min_rating = min(df['rating'])

# Nilai maksimal rating
max_rating = max(df['rating'])

df = df.sample(frac=1, random_state=42)

# Membuat variabel x untuk mencocokkan data user dan cellphone menjadi satu value
x = df[['user', 'cellphone']].values

# Membuat variabel y untuk membuat rating dari hasil
y = df['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_cellphones, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_phone = num_cellphones
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.phone_embedding = layers.Embedding( # layer embeddings phone
        num_cellphones,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.phone_bias = layers.Embedding(num_cellphones, 1) # layer embedding phone bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    phone_vector = self.phone_embedding(inputs[:, 1]) # memanggil layer embedding 3
    phone_bias = self.phone_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_phone = tf.tensordot(user_vector, phone_vector, 2)

    x = dot_user_phone + user_bias + phone_bias

    return tf.nn.sigmoid(x) # activation sigmoid

# Buat model
model = RecommenderNet(num_users, num_cellphones, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (x_val, y_val)
)

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

print(f"Final RMSE Train: {history.history['root_mean_squared_error'][-1]:.4f}")
print(f"Final RMSE Test: {history.history['val_root_mean_squared_error'][-1]:.4f}")

cellphone_df = cellphone_new
df = pd.read_csv('/content/dataset/cellphones ratings.csv')

# Mengambil sample user
user_id = df.user_id.sample(1).iloc[0]
cellphone_reviewed_by_user = df[df.user_id == user_id]

cellphone_not_reviewed = cellphone_df[~cellphone_df['id'].isin(cellphone_reviewed_by_user.cellphone_id.values)]['id']
cellphone_not_reviewed = list(
    set(cellphone_not_reviewed)
    .intersection(set(cellphone_to_cellphone_encoded.keys()))
)

cellphone_not_reviewed = [[cellphone_to_cellphone_encoded.get(x)] for x in cellphone_not_reviewed]
user_encoder = user_to_user_encoded.get(user_id)
user_cellphone_array = np.hstack(
    ([[user_encoder]] * len(cellphone_not_reviewed), cellphone_not_reviewed)
)

ratings = model.predict(user_cellphone_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_cellphone_ids = [
    cellphone_encoded_to_cellphone.get(cellphone_not_reviewed[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('cellphone with high ratings from user')
print('----' * 8)

top_cellphone_user = (
    cellphone_reviewed_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .cellphone_id.values
)

cellphone_df_rows = cellphone_df[cellphone_df['id'].isin(top_cellphone_user)]
for row in cellphone_df_rows.itertuples():
    print(row.brand, ':', row.model)

print('----' * 8)
print('Top 10 cellphone recommendation')
print('----' * 8)

recommended_cellphone = cellphone_df[cellphone_df['id'].isin(recommended_cellphone_ids)]
for row in recommended_cellphone.itertuples():
    print(row.brand, ':', row.model)