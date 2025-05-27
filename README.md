# Laporan Proyek Machine Learning - Jessindy Tanuwijaya

![Man holding phone](https://raw.githubusercontent.com/jessdytan/phone-recommendation-system/main/images/jonas-leupe-wK-elt11pF0-unsplash.jpg)

## Project Overview
Pesatnya perkembangan pasar ponsel pintar menghadirkan tantangan signifikan bagi konsumen dalam memilih produk yang paling sesuai di tengah beragamnya spesifikasi dan harga. Kebingungan dan waktu yang sering terbuang dalam proses seleksi ini menyoroti kebutuhan mendesak akan solusi yang lebih efektif. Sistem rekomendasi menawarkan pendekatan cerdas untuk menyederhanakan pencarian ini, dengan tujuan meningkatkan kepuasan pengguna dan memfasilitasi keputusan pembelian yang lebih tepat sasaran.

Penelitian ilmiah secara konsisten menunjukkan bahwa metode inti dalam sistem rekomendasi, seperti Collaborative Filtering dan Content-Based Filtering, tetap efektif dalam menyediakan saran yang personal dan relevan, bahkan ketika diintegrasikan dengan teknik-teknik modern (Ricci et al., 2015; Zhang et al., 2019)[^1][^2]. Oleh karena itu, proyek ini bertujuan untuk merancang dan mengembangkan sistem rekomendasi ponsel yang memanfaatkan prinsip-prinsip dasar tersebut, guna membantu pengguna menemukan produk yang optimal dan paling sesuai dengan kebutuhan serta preferensi individual mereka.

## Business Understanding

### Problem Statements

1. Bagaimana memberikan rekomendasi ponsel yang relevan dan sesuai dengan preferensi pengguna?
2. Bagaimana mengoptimalkan akurasi rekomendasi dengan memanfaatkan data ulasan dan rating pengguna?
3. Bagaimana menghadirkan rekomendasi ponsel yang personal dan mudah dipahami oleh pengguna?

### Goals

1. Membangun sistem rekomendasi ponsel yang memberikan Top-N rekomendasi berdasarkan preferensi dan data pengguna.
2. Menggunakan data ulasan dan rating untuk meningkatkan akurasi rekomendasi.
3. Membandingkan pendekatan content-based dan collaborative filtering dalam sistem rekomendasi ponsel.

### Solution Approach
- Content-Based Filtering: Sistem merekomendasikan ponsel berdasarkan kemiripan fitur teknis dan ulasan ponsel yang sebelumnya disukai oleh pengguna.
- Collaborative Filtering: Sistem merekomendasikan ponsel berdasarkan pola preferensi pengguna lain yang memiliki kesamaan minat dengan pengguna target.

## Data Understanding

| Jenis Informasi | Keterangan                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| Format          | .csv                                                                                                    |
| **Title**       | Cellphones Recommendations                                                                                   |
| **Source**      | Kaggle                                                                                                  |
| **Maintainer**  | meirnizri                                                                                              |
| **License**     | Open Data Commons Open Database License (ODbL) v1.0                                                                                            |
| **Visibility**  | Publik                                                                                                  |
| **Tags**        | Pre-Trained Model, Electronics, E-Commerce Services, Mobile and Wireless, Recommender Systems |
| **Usability**   | 10.00                                                                                                    |

Dataset yang digunakan adalah [Cellphones Recommendations](https://www.kaggle.com/datasets/meirnizri/cellphones-recommendations) dari Kaggle. Dataset terdiri dari tiga file utama, yaitu:
- cellphones data.csv – 33 baris dengan 14 kolom fitur cellphone.
- cellphones ratings.csv – 990 baris dengan 3 kolom fitur rating.
- cellphones users.csv – 99 baris dengan 4 kolom fitur identitas.

Dataset ini digunakan untuk membangun sistem rekomendasi ponsel berdasarkan preferensi pengguna. Dataset mencakup ribuan entri ponsel yang mencerminkan variasi dalam merek, harga, rating pengguna, ulasan teks, dan spesifikasi teknis seperti RAM, kamera, dan baterai. Tujuan utama dari dataset ini adalah memahami preferensi konsumen dan memberikan rekomendasi ponsel yang relevan, misalnya berdasarkan rating tinggi, harga terjangkau, atau fitur yang diinginkan pengguna.

### Fitur-fitur pada dataset:
1. Dataset cellphones data.csv
    | Fitur              | Deskripsi                                                                 |
    |--------------------|---------------------------------------------------------------------------|
    | cellphone_id        | ID unik untuk setiap ponsel                                               |
    | brand               | Merek ponsel (misalnya: Samsung, Xiaomi, Apple)                          |
    | model               | Model ponsel tertentu dari brand terkait                                  |
    | operating system    | Sistem operasi yang digunakan (misalnya: Android, iOS)                    |
    | internal memory     | Kapasitas memori internal (dalam GB)                                      |
    | RAM                 | Kapasitas RAM (dalam GB)                                                  |
    | performance         | Skor performa keseluruhan (dalam bentuk skor numerik)                     |
    | main camera         | Resolusi kamera utama (dalam Megapiksel)                                  |
    | selfie camera       | Resolusi kamera depan (dalam Megapiksel)                                  |
    | battery size        | Kapasitas baterai (dalam mAh)                                             |
    | screen size         | Ukuran layar (dalam inci)                                                 |
    | weight              | Berat ponsel (dalam gram)                                                 |
    | price               | Harga ponsel (dalam satuan lokal, misalnya IDR atau USD)                  |
    | release date        | Tanggal rilis ponsel  |

2. Dataset cellphones ratings.csv
    | Fitur         | Deskripsi                                                                 |
    |---------------|---------------------------------------------------------------------------|
    | user_id       | ID unik pengguna yang memberikan penilaian                               |
    | cellphone_id  | ID ponsel yang dinilai oleh pengguna                                     |
    | rating        | Nilai rating yang diberikan pengguna terhadap ponsel (skala 1–10) |

3. Dataset cellphones users.csv
    | Fitur       | Deskripsi                                                               |
    |-------------|-------------------------------------------------------------------------|
    | user_id     | ID unik pengguna                                                       |
    | age         | Usia pengguna                                                          |
    | gender      | Jenis kelamin pengguna (misalnya: Male, Female)                        |
    | occupation  | Pekerjaan pengguna (misalnya: Manager, Engineer, dsb.)                 |



### Contoh Data (Head):
1. cellphones data.csv
    | cellphone_id | brand | model               | operating system | internal memory | RAM | performance | main camera | selfie camera | battery size | screen size | weight | price | release date |
    |--------------|--------|----------------------|------------------|------------------|-----|-------------|--------------|----------------|---------------|--------------|--------|--------|----------------|
    | 0            | Apple | iPhone SE (2022)     | iOS              | 128              | 4   | 7.23        | 12           | 7              | 2018          | 4.7          | 144    | 429    | 18/03/2022     |
    | 1            | Apple | iPhone 13 Mini       | iOS              | 128              | 4   | 7.72        | 12           | 12             | 2438          | 5.4          | 141    | 699    | 24/09/2021     |
    | 2            | Apple | iPhone 13            | iOS              | 128              | 4   | 7.75        | 12           | 12             | 3240          | 6.1          | 174    | 699    | 24/09/2021     |
    | 3            | Apple | iPhone 13 Pro        | iOS              | 256              | 6   | 7.94        | 12           | 12             | 3065          | 6.1          | 204    | 999    | 24/09/2021     |
    | 4            | Apple | iPhone 13 Pro Max    | iOS              | 256              | 6   | 8.01        | 12           | 12             | 4352          | 6.7          | 240    | 1199   | 24/09/2021     |


2. cellphones ratings.csv
    | user_id | cellphone_id | rating |
    |---------|---------------|--------|
    | 0       | 30            | 1      |
    | 0       | 5             | 3      |
    | 0       | 10            | 9      |
    | 0       | 9             | 3      |
    | 0       | 23            | 2      |

3. cellphones users.csv
    | user_id | age | gender | occupation         |
    |---------|-----|--------|--------------------|
    | 0       | 38  | Female | Data analyst       |
    | 1       | 40  | Female | team worker in it  |
    | 6       | 55  | Female | IT                 |
    | 8       | 25  | Female | Manager            |
    | 10      | 23  | Male   | worker             |

### Kondisi Data:
- Duplikat: 
    - cellphones data.csv :  Dataset **tidak mengandung nilai duplikat** pada kolom manapun.
    - cellphones ratings.csv : Dataset **tidak mengandung nilai duplikat** pada kolom manapun.
    - cellphones users.csv : Dataset **tidak mengandung nilai duplikat** pada kolom manapun.


- Nilai Kosong:
    - cellphones data.csv :  Dataset **tidak mengandung nilai hilang** pada kolom manapun.
    - cellphones ratings.csv : Dataset **tidak mengandung nilai hilang** pada kolom manapun.
    - cellphones users.csv : Ada 10 data `occupation` yang hilang.
    **Penanganan**: baris yang memiliki data yang hilang ini akan di drop.

- Tipe Data: 
    1) cellphones data.csv : hanya `release date` yang tidak mempunyai tipe data yang sesuai.
        **Penanganan**: mengubah kolom `release date` menjadi datetime.
        | Kolom             | Tipe Data |
        |-------------------|-----------|
        | cellphone_id      | int64     |
        | brand             | object    |
        | model             | object    |
        | operating system  | object    |
        | internal memory   | int64     |
        | RAM               | int64     |
        | performance       | float64   |
        | main camera       | int64     |
        | selfie camera     | int64     |
        | battery size      | int64     |
        | screen size       | float64   |
        | weight            | int64     |
        | price             | int64     |
        | release date      | object    |   
    2) cellphones ratings.csv: Semua mempunyai tipe data yang sesuai.
        | Kolom         | Tipe Data |
        |---------------|-----------|
        | user_id       | int64     |
        | cellphone_id  | int64     |
        | rating        | int64     |
    3) cellphones users.csv: Semua mempunyai tipe data yang sesuai.
        | Kolom      | Tipe Data |
        |------------|-----------|
        | user_id    | int64     |
        | age        | int64     |
        | gender     | object    |
        | occupation | object    |

### Exploratory Data Analysis (EDA)

- Distribusi Operating System Ponsel
    ![Distribusi OS](https://raw.githubusercontent.com/jessdytan/phone-recommendation-system/main/images/os_distribution.png)

    **Analisis**:
    Analisis dari grafik ini menyimpulkan bahwa sistem operasi **Android lebih banyak digunakan** dibandingkan dengan iOS dalam kelompok pengguna yang datanya disajikan. Perbedaan jumlah pengguna antara kedua sistem operasi tersebut cukup mencolok.

- Distribusi Rating Ponsel
  ![Distribusi Rating](https://raw.githubusercontent.com/jessdytan/phone-recommendation-system/main/images/cellphone_rating.png)

  **Analisis**:
  Mayoritas ponsel dalam sampel ini memiliki **rating yang baik** hingga sangat baik (terutama di sekitar rating 7 dan 8). Terdapat jumlah yang lebih kecil untuk ponsel dengan rating rendah. Keberadaan rating "**18**" dengan jumlah yang sangat minim menunjukkan bahwa data tersebut adalah data **outlier**.
 
- Ponsel Populer.
  ![Ponsel Populer](https://raw.githubusercontent.com/jessdytan/phone-recommendation-system/main/images/popular_cellphone.png)

  **Analisis**:
    Visualisasi menunjukkan bahwa **Moto G Play (2021) adalah ponsel yang paling menarik perhatian** atau paling banyak diulas oleh pengguna dalam dataset ini. Model-model dari berbagai merek seperti Samsung (Galaxy A32, Galaxy Z Flip 3, Galaxy S22 Ultra), Google (Pixel 6), Xiaomi (11T Pro, Redmi Note 11, Poco F4), dan Apple (iPhone 13 Pro Max) juga masuk dalam daftar ponsel yang populer untuk direview. Tingginya jumlah review bisa mengindikasikan popularitas, volume penjualan yang tinggi, atau ketertarikan khusus dari komunitas teknologi terhadap model-model tersebut.

- Distribusi Rata-Rata Rating dengan Pekerjaan User
  ![Distribusi Gender](https://raw.githubusercontent.com/jessdytan/phone-recommendation-system/main/images/occupation_distribution.png)

  **Analisis**:
    Visualisasi menunjukkan terdapat **perbedaan yang cukup besar dalam rata-rata rating yang dikaitkan dengan berbagai profesi**. Pekerjaan di bidang informasi, layanan kesehatan (healthcare), dan bisnis cenderung mendapatkan atau memberikan rata-rata rating yang sangat tinggi. Sebaliknya, profesi seperti guru (teacher), pemasaran (marketing), dan beberapa peran penjualan (sales) menunjukkan rata-rata rating yang jauh lebih rendah dalam dataset ini. **Beberapa pekerjaan dapat dikelompokkan menjadi satu kelompok** seperti it, IT, team worker in it.

## Data Preparation

Pada tahap ini, dilakukan beberapa teknik untuk menyiapkan data sebelum masuk ke proses pemodelan. Urutan dan penjelasan tiap langkah sebagai berikut:

1. Menggabungkan ketiga dataset menjadi satu dataframe
    Menggabungkan dataset `cellphones data.csv`, `cellphones ratings.csv`, `cellphones users.csv` menjadi satu dataframe. Setiap dataset ini berisikan informasi yang berbeda mengenai entitas yang sama atau terkait.
    - **Alasan**: Untuk mengkonsolidasikan semua informasi yang relevan ke dalam satu tempat.


2. Mengecek Data Duplikat
   Dilakukan pengecekan data duplikat untuk memastikan tidak ada pengulangan entri yang dapat memengaruhi akurasi model.
    Setelah dilakukan pengecekan, ternyata tidak ada data duplikat dalam dataset.
   - **Alasan**: Duplikat dapat menyebabkan bias dalam model dan menurunkan performa karena informasi yang sama dihitung lebih dari sekali.


3. Mengubah format data `release date` ke dalam bentuk datetime
    Kolom `release date`, yang awalnya tersimpan sebagai object, dikonversi menjadi format datetime standar. Format ini memungkinkan komputer untuk memahami dan memanipulasi tanggal dan waktu secara benar.
    - **Alasan**: Konversi ke format datetime memungkinkan operasi berbasis waktu yang akurat.


4. Menangani Nilai yang Hilang (Missing Values)
  Setelah dilakukan identifikasi dalam dataset, ternyata terdapat kolom `occupation` yang tidak memiliki nilai (kosong atau NaN). Oleh karena itu, baris-baris di mana kolom occupation ini kemudian dihapus (di-drop).
   - **Alasan**: Nilai kosong bisa mengganggu proses training model dan menurunkan kualitas prediksi.
   - **Penanganan**: Drop baris yang kolom `occupation` nya kosong.


5. Menangani Outlier
   Setelah dilakukan visualisasi distribusi rating ponsel, ternyata terdapat data outlier berupa rating "**18**" yang tidak masuk akal dalam skala rating ponsel yang umum. Outlier yang telah dideteksi tersebut kemudian dihapus dari dataset.  
   - **Alasan**: Outlier dapat memengaruhi distribusi data dan membuat model belajar pola yang tidak umum (noise).
   - **Penanganan**: Drop baris yang memiliki rating **18** tersebut.
  

6. Split Data: Training dan Test Set (80:20)
   Keseluruhan dataset yang telah dibersihkan dan diproses dibagi menjadi dua bagian yang saling eksklusif: data latih (training set) yang lebih besar (80% dari total data) dan data uji (test set) yang lebih kecil (20% dari total data).
   - **Alasan**: Pembagian ini penting untuk mengevaluasi performa model secara objektif terhadap data yang belum pernah dilihat sebelumnya.


## Modeling and Result
Pada tahap ini, dikembangkan dua jenis sistem rekomendasi untuk memberikan saran ponsel kepada pengguna menggunakan content-based filtering dan collaborative-filtering. Berikut adalah penjelasan masing-masing sistem rekomendasi nya:

1. Content-Based Filtering : Merekomendasikan item berdasarkan **kemiripan atribut** atau **fitur item** itu sendiri 
    - Tahapan proses:
        -  **Representasi Fitur**: Setiap ponsel direpresentasikan sebagai vektor fitur berdasarkan atributnya (brand, model, Operating System, Memory, RAM). Fitur kategorikal diubah menjadi vektor numerik menggunakan TF-IDF.
        -  **Perhitungan Kemiripan**: Kemiripan antar ponsel dihitung menggunakan metrik Cosine Similarity pada vektor fitur nya. Cosine Similarity mengukur kosinus sudut antara dua vektor, yang menunjukkan seberapa mirip orientasinya (dan dengan demikian, seberapa mirip fitur ponselnya).
        -  **Generasi Rekomendasi (Top-N)**: 
            1. Ambil satu ponsel yang telah disukai/dilihat pengguna (atau sebagai ponsel referensi).
            2. Hitung kemiripan ponsel referensi tersebut dengan semua ponsel lain dalam dataset berdasarkan fiturnya.
            3. Urutkan ponsel berdasarkan skor kemiripan tertinggi.
            4. Sajikan N ponsel teratas (dalam penyelesaian ini Top-10) yang belum pernah berinteraksi dengan pengguna sebagai rekomendasi.
    - Hasil: Model berhasil merekomendasikan ponsel yang memiliki kesamaan fitur dengan ponsel yang disukai pengguna.
        Berikut adalah output untuk rekomendasi model `iPhone 13 Mini`
        | model              | brand | os  | memory | ram |
        |--------------------|-------|-----|--------|-----|
        | iPhone 13          | Apple | iOS | 128    | 4   |
        | iPhone SE (2022)   | Apple | iOS | 128    | 4   |
        | iPhone XR          | Apple | iOS | 64     | 3   |
        | iPhone 13 Pro      | Apple | iOS | 256    | 6   |
        | iPhone 13 Pro Max  | Apple | iOS | 256    | 6   |

    - Kelebihan:
        1. **Tidak Memerlukan Data Pengguna Lain (No Cold Start untuk Item Baru)**: Dapat merekomendasikan item baru selama item tersebut memiliki deskripsi fitur yang memadai.
        2. **Transparan**: Rekomendasi dapat dijelaskan berdasarkan fitur spesifik yang mirip (misalnya, "Anda direkomendasikan ponsel X karena sama-sama memiliki RAM besar dan OS Android seperti ponsel Y yang Anda sukai").
        3. **Personalisasi Spesifik**: Dapat menangkap preferensi spesifik pengguna terhadap atribut tertentu.
    - Kekurangan:
        1. **Keterbatasan Fitur (Feature Engineering)**: Kualitas dari hasil rekomendasi sangat bergantung pada kualitas dan kelengkapan fitur yang digunakan. Jika fitur tidak deskriptif, rekomendasi akan buruk.
        2. **Over-Specialization (Filter Bubble)**: Cenderung merekomendasikan item yang sangat mirip dengan apa yang sudah disukai pengguna, sehingga kurang ada penemuan item di luar zona nyaman pengguna.
        

2. Collaborative-Based Filtering: Merekomendasikan item berdasarkan kemiripan preferensi antar pengguna (user-based) 
    - Tahapan proses:
        - **Menggunakan dataframe `rating`**
        - **Encoding `user_id`, `cellphone_id`**
        - **Membuat Arsitektur Model Neural Network (RecommenderNet)**:
            1. Struktur model mencakup layer Embedding untuk pengguna dan ponsel (beserta layer bias masing-masing) untuk memproyeksikan ID ke ruang vektor.
            2. Forward pass model menghitung dot product antara embedding pengguna dan ponsel, menambahkan bias, lalu menerapkan aktivasi sigmoid untuk prediksi.
        - **Kompilasi dan latih model menggunakan data latih, dengan `batch_size`=8 dan `epochs`=100.**
        - **Generasi Rekomendasi (Top-N)**: 
            1. Untuk pengguna tertentu, model memprediksi skor preferensi untuk semua (atau sejumlah besar kandidat) ponsel yang belum pernah berinteraksi dengan pengguna tersebut.
            2. Ponsel-ponsel tersebut diurutkan berdasarkan skor prediksi dari yang tertinggi ke terendah.
            3. N ponsel teratas dari daftar yang telah diurutkan tersebut disajikan sebagai rekomendasi. (pada kasus ini digunakan untuk mengeluarkan output n=10)
        
    - Hasil: 
        ``` bash
        Showing recommendations for users: 234
        ===========================
        cellphone with high ratings from user
        --------------------------------
        Apple : iPhone XR
        Samsung : Galaxy S22
        Samsung : Galaxy Z Flip 3
        Apple : iPhone 13 Mini
        Xiaomi : 11T Pro
        --------------------------------
        Top 10 cellphone recommendation
        --------------------------------
        Vivo : X80 Pro
        Oppo : Find X5 Pro
        OnePlus : Nord 2T
        Apple : iPhone 13 Pro
        Apple : iPhone 13 Pro Max
        Apple : iPhone SE (2022)
        Google : Pixel 6 Pro 
        Samsung : Galaxy S22 Ultra
        Xiaomi : 12 Pro
        Apple : iPhone 13
        ```
    - Kelebihan: 
        1. **Tidak Memerlukan Analisis Fitur**: Collaborative filtering bekerja berdasarkan interaksi historis pengguna dengan rating.
        2. **Kemampuan Menemukan Item Baru yang Beragam (Serendipity)**: Dapat merekomendasikan item yang mungkin sangat berbeda secara fitur dari apa yang pernah disukai pengguna di masa lalu.
    - Kekurangan:
        1. **Cold Start Problem**: Sistem kesulitan memberikan rekomendasi yang akurat untuk pengguna baru karena belum ada histori interaksi mereka yang bisa dicocokkan dengan pengguna lain atau item baru yang belum mendapatkan cukup interaksi.
        2. **Popularity Bias (Bias Popularitas)**: Cenderung merekomendasikan item yang sudah populer karena item populer secara alami memiliki lebih banyak data interaksi

## Evaluation
Tahap evaluasi bertujuan untuk mengukur kinerja sistem rekomendasi ponsel yang telah dibangun, khususnya dalam kemampuannya memprediksi preferensi pengguna secara akurat. Evaluasi ini penting untuk memahami sejauh mana solusi yang diusulkan berhasil menjawab permasalahan dan mencapai tujuan yang telah ditetapkan.

### Content-Based Filtering
#### Metrik Evaluasi
Untuk mengukur kinerja dari sistem rekomendasi content-based filtering, akan digunakan beberapa metrik evaluasi. Metrik ini membantu mengevaluasi kualitas rekomendasi yang dihasilkan, terutama dari segi relevansi dan urutan.
 1. Precision@k

     **Precision@k** mengukur proporsi item yang relevan di antara top-\(k\) item yang direkomendasikan.
    - Formula:
      
    $\displaystyle \text{Precision@k} = \frac{\text{Jumlah item relevan dalam top-}k}{k}$
    - Cara Kerja:
    Precision@k menghitung seberapa banyak dari \(k\) rekomendasi teratas yang benar-benar relevan untuk pengguna. Nilai precision yang tinggi menunjukkan bahwa sistem memberikan rekomendasi yang akurat.


3. Recall@k

    **Recall@k** mengukur proporsi item relevan yang berhasil ditemukan dalam \(k\) rekomendasi.
    
    - Formula:
   
    $\displaystyle \text{Recall@k} = \frac{\text{Jumlah item relevan dalam top-}k}{\text{Jumlah total item relevan}}$
    - Cara Kerja:
    Recall@k fokus pada seberapa banyak item relevan yang ditemukan oleh sistem dari semua item relevan yang tersedia. Nilai recall tinggi menunjukkan sistem mampu mencakup banyak item relevan.


4. F1 Score@k

    **F1 Score@k** merupakan harmonic mean dari Precision@k dan Recall@k, memberikan keseimbangan antara keduanya.
    
    - Formula:
   
    $\displaystyle\text{F1@k} = 2 \cdot \frac{\text{Precision@k} \cdot \text{Recall@k}}{\text{Precision@k} + \text{Recall@k}}$
    
    - Cara Kerja:
    F1 Score digunakan ketika kita ingin mempertimbangkan baik ketepatan (precision) maupun kelengkapan (recall) dari hasil rekomendasi. Skor ini berguna jika ada trade-off antara precision dan recall.

5. Normalized Discounted Cumulative Gain (NDCG@k)

    **NDCG@k** digunakan untuk mengukur kualitas urutan rekomendasi dengan mempertimbangkan posisi item relevan. Semakin tinggi posisi item relevan, semakin besar pengaruhnya terhadap skor.
    - Formula:
      
        $\displaystyle\text{DCG@k} = \sum_{i=1}^{k} \frac{2^{rel_i} - 1}{\log_2(i + 1)}$
      
        $\displaystyle\text{IDCG@k} = \text{DCG dari urutan ideal relevansi}$
      
        $\displaystyle\text{NDCG@k} = \frac{\text{DCG@k}}{\text{IDCG@k}}$

    - Cara Kerja:
    NDCG menghitung seberapa baik urutan rekomendasi berdasarkan relevansi item yang muncul pada posisi tertentu. Sistem yang merekomendasikan item relevan lebih awal mendapatkan skor lebih tinggi.

#### Hasil Proyek
Untuk pengujian ini, kami mengambil contoh skenario di mana model memberikan rekomendasi berdasarkan query "iPhone 13 Mini". Daftar item yang direkomendasikan oleh model adalah sebagai berikut:
```
recommended_items = ['iPhone 13', 'iPhone SE (2022)', 'iPhone XR', 'iPhone 13', 'iPhone 13']
```

Sementara itu, daftar item yang relevan (item "true" yang seharusnya direkomendasikan) adalah:
```
true_items = ['iPhone 13', 'iPhone 13 Pro', 'iPhone 12 Mini']
```

Berdasarkan perbandingan antara recommended_items dan true_items, hasil metrik evaluasi adalah sebagai berikut:
- Precision@5: 0.4
- Recall@5: 0.6666666666666666
- F1 Score@5: 0.5
- NDCG@5: 0.671386072533041

Secara keseluruhan, hasil ini memberikan wawasan awal tentang kinerja model rekomendasi. Meskipun model berhasil mengidentifikasi sebagian besar item relevan, terdapat peluang untuk meningkatkan presisi rekomendasi dan penempatan item relevan di posisi yang lebih tinggi. 

### Collaborative-Based Filtering:
Untuk mengukur kinerja sistem rekomendasi berbasis collaborative filtering, digunakan beberapa metrik evaluasi. Metrik-metrik ini bertujuan untuk menilai kualitas rekomendasi yang dihasilkan, khususnya dari segi relevansi item yang direkomendasikan dan urutan penyajiannya. Dengan menggunakan metrik evaluasi ini, kita dapat mengetahui     seberapa efektif sistem dalam memberikan rekomendasi yang sesuai dengan preferensi pengguna.

- **RMSE**
  RMSE adalah metrik standar untuk mengukur rata-rata besarnya kesalahan antara nilai yang diprediksi oleh model dengan nilai aktual. Dalam konteks sistem rekomendasi, RMSE mengukur seberapa jauh rata-rata prediksi rating model dari rating yang sebenarnya diberikan oleh pengguna.
  
  $\displaystyle \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$

  Di mana:

  * $\displaystyle n$ adalah jumlah total data poin (rating) yang dievaluasi.
  * $\displaystyle y_i$ adalah rating aktual yang diberikan oleh pengguna untuk item ke-$\displaystyle i$.
  * $\displaystyle \hat{y}_i$ adalah rating yang diprediksi oleh model untuk item ke-$\displaystyle i$.
  
  ### Cara Kerja dan Interpretasi:
  
  1.  Untuk setiap pasang rating aktual dan prediksi, selisihnya ($\displaystyle (y_i - \hat{y}_i)$) dihitung.
  2.  Selisih tersebut dikuadratkan ($(y_i - \hat{y}_i)^2$). Pengkuadratan ini memberikan bobot lebih pada kesalahan yang besar dan menghilangkan tanda negatif.
  3.  Nilai rata-rata dari kesalahan kuadrat tersebut dihitung ($\displaystyle \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$).
  4.  Akhirnya, akar kuadrat dari rata-rata tersebut diambil untuk mengembalikan unit kesalahan ke skala yang sama dengan rating asli.
     
    

### Hasil Proyek
![RMSE Results](https://raw.githubusercontent.com/jessdytan/phone-recommendation-system/main/images/rmse_metrics.png)

| | RMSE|
|-----|------|
| Train| 0.1481 |
| Test | 0.1621 |

Nilai RMSE Train sebesar **0.1481** menunjukkan kemampuan model yang sangat baik dalam mempelajari data pelatihan. RMSE Test sebesar **0.1621** mengindikasikan kinerja generalisasi yang kuat pada data baru, dengan selisih minimal dari RMSE Train, yang menandakan tidak adanya overfitting signifikan.
Dengan RMSE Test yang rendah, dapat disimpulkan bahwa model Collaborative Filtering ini **efektif** dan **akurat** dalam memprediksi preferensi pengguna dan memberikan rekomendasi yang relevan.


### Evaluasi Terhadap Business Understanding
1. **Relevansi Rekomendasi dan Pengalaman Pengguna Terancam Overfitting**: Grafik menunjukkan bahwa melatih model terlalu lama (menyebabkan overfitting) akan menghasilkan rekomendasi yang kurang relevan bagi pengguna secara umum dan pada situasi baru, sehingga menurunkan kualitas pengalaman pengguna dan kepercayaan terhadap sistem. Model yang optimal (berhenti pada performa test set terbaik) krusial untuk menjaga relevansi.
2. **Akurasi Nyata vs. Akurasi Semu dalam Pemanfaatan Data Rating**: Overfitting memberikan ilusi akurasi tinggi pada data latih, namun akurasi sebenarnya pada data pengguna baru (terlihat dari performa test set) lebih rendah. Untuk benar-benar mengoptimalkan pemanfaatan data rating demi akurasi, fokus harus pada performa model pada data yang belum pernah dilihat, bukan sekadar performa pada data latih.
3. **Efisiensi Sumber Daya untuk Hasil Optimal**: Melanjutkan pelatihan model melewati titik di mana performa pada test set tidak lagi membaik (seperti yang ditunjukkan grafik) adalah pemborosan sumber daya komputasi dan waktu. Dari sudut pandang bisnis, ini berarti biaya yang tidak perlu untuk hasil yang justru lebih buruk dalam praktiknya.
4. **Dampak Langsung pada Pencapaian Tujuan Business Goals**: Rekomendasi yang tidak akurat akibat overfitting akan menghambat pencapaian tujuan bisnis seperti peningkatan keterlibatan pengguna, konversi, dan loyalitas. Model yang generalisasinya baik adalah fondasi untuk rekomendasi yang efektif mendukung tujuan tersebut.
5. **Validitas Perbandingan Antar Pendekatan Rekomendasi**: Saat membandingkan efektivitas pendekatan yang berbeda (misalnya, Content-Based vs. Collaborative Filtering sesuai Goal 3 Anda), grafik ini menekankan pentingnya membandingkan model berdasarkan performa optimalnya pada data validasi/uji. Membandingkan model yang satu overfitting dengan yang lain tidak akan memberikan kesimpulan yang valid mengenai pendekatan mana yang terbaik untuk bisnis Anda.

---
**Referensi:**
[^1]: Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender systems: introduction and challenges. In L. Rokach, B. Shapira, F. Ricci, & P. B. Kantor (Eds.), Recommender Systems Handbook (2nd ed., pp. 1-34). Springer, Boston, MA.
[^2]: Zhang, S., Yao, L., Sun, A., & Tay, Y. (2019). Deep Learning based Recommender System: A Survey and New Perspectives. ACM Computing Surveys (CSUR), 52(1), Article 5, 1–38.
