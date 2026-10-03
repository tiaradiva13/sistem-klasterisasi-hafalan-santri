# Prompt Log AI
# Sistem Klasterisasi Hafalan Santri


## 1. Pendahuluan

Dokumen Prompt Log AI berisi dokumentasi penggunaan Artificial Intelligence (AI) sebagai alat bantu dalam proses perancangan Sistem Klasterisasi Hafalan Santri.

AI digunakan untuk membantu proses analisis kebutuhan sistem, penyusunan arsitektur aplikasi, perancangan database, pembuatan spesifikasi API, serta penyusunan dokumen High-Level Design (HLD) dan Low-Level Design (LLD).

Seluruh hasil dari AI digunakan sebagai referensi awal dan tetap dilakukan penyesuaian berdasarkan kebutuhan sistem yang dikembangkan.


---

# 2. Tujuan Penggunaan AI


Penggunaan AI dalam proses perancangan sistem bertujuan untuk:


1. Membantu menyusun struktur dokumen desain perangkat lunak.

2. Membantu menentukan rancangan arsitektur sistem.

3. Membantu membuat rancangan database.

4. Membantu menyusun modul aplikasi.

5. Membantu membuat spesifikasi API.

6. Membantu melakukan evaluasi rancangan sistem.


---

# 3. Prompt Perancangan High-Level Design (HLD)


## Tujuan

Membuat rancangan umum sistem yang mencakup arsitektur aplikasi, modul utama, alur data, dan hubungan antar komponen.


## Prompt yang Digunakan


```
Buatkan rancangan High-Level Design (HLD) untuk aplikasi Sistem Klasterisasi Hafalan Santri berbasis web.

Sistem digunakan untuk mengelola data santri, mencatat perkembangan hafalan, dan melakukan pengelompokan santri menggunakan algoritma clustering.

Rancangan harus mencakup arsitektur sistem, diagram alur data, desain modul, aktor sistem, keamanan sistem, dan deployment architecture.
```


## Hasil dari AI


AI menghasilkan rancangan:

- Arsitektur tiga lapisan (Presentation Layer, Application Layer, Data Layer).
- Modul authentication.
- Modul data santri.
- Modul hafalan.
- Modul clustering.
- Modul dashboard.
- Diagram alur data sistem.


## Evaluasi Hasil


Hasil rancangan AI digunakan sebagai dasar penyusunan dokumen HLD kemudian disesuaikan dengan kebutuhan aplikasi Sistem Klasterisasi Hafalan Santri.


---


# 4. Prompt Perancangan Low-Level Design (LLD)


## Tujuan

Membuat rancangan teknis sistem yang menjelaskan detail implementasi aplikasi.


## Prompt yang Digunakan


```
Buatkan rancangan Low-Level Design (LLD) awal untuk aplikasi Sistem Klasterisasi Hafalan Santri.

Dokumen harus mencakup desain database, struktur tabel, relasi antar tabel, desain modul, algoritma clustering, spesifikasi API REST, struktur folder aplikasi, dan rancangan pengujian sistem.
```


## Hasil dari AI


AI menghasilkan rancangan:

- Struktur database users, santri, hafalan, dan cluster result.
- Relasi antar tabel.
- Detail modul aplikasi.
- Spesifikasi endpoint API.
- Struktur folder aplikasi.
- Rencana pengujian sistem.


## Evaluasi Hasil


Hasil AI digunakan sebagai rancangan awal dan dilakukan penyesuaian agar sesuai dengan kebutuhan pengembangan aplikasi.


---


# 5. Prompt Perancangan Database


## Tujuan

Membantu menentukan struktur penyimpanan data yang diperlukan oleh sistem.


## Prompt yang Digunakan


```
Buatkan desain database untuk aplikasi Sistem Klasterisasi Hafalan Santri.

Database harus dapat menyimpan data pengguna, data santri, data perkembangan hafalan, dan hasil proses clustering.
```


## Hasil dari AI


AI menghasilkan beberapa tabel utama:


1. Users

Digunakan untuk menyimpan data akun pengguna.


2. Santri

Digunakan untuk menyimpan identitas santri.


3. Hafalan

Digunakan untuk menyimpan perkembangan hafalan.


4. Cluster Result

Digunakan untuk menyimpan hasil pengelompokan santri.


## Evaluasi Hasil


Struktur database digunakan sebagai rancangan awal dan dapat dikembangkan kembali sesuai kebutuhan implementasi.


---


# 6. Prompt Perancangan API


## Tujuan

Membuat rancangan komunikasi antara frontend, backend, dan database.


## Prompt yang Digunakan


```
Buatkan spesifikasi REST API untuk Sistem Klasterisasi Hafalan Santri.

API harus mencakup autentikasi pengguna, pengelolaan data santri, pengelolaan data hafalan, dan proses clustering.
```


## Hasil dari AI


AI menghasilkan rancangan endpoint:


```
POST /api/login

GET /api/santri

POST /api/santri

PUT /api/santri/{id}

DELETE /api/santri/{id}

POST /api/hafalan

POST /api/clustering
```


## Evaluasi Hasil


Spesifikasi API digunakan sebagai gambaran komunikasi antar komponen sistem.


---


# 7. Prompt Perancangan Algoritma Clustering


## Tujuan

Membantu menjelaskan mekanisme proses pengelompokan data santri.


## Prompt yang Digunakan


```
Jelaskan implementasi algoritma K-Means Clustering untuk sistem pengelompokan santri berdasarkan perkembangan hafalan.
```


## Hasil dari AI


AI menjelaskan tahapan:


1. Pengumpulan dataset.

2. Preprocessing data.

3. Normalisasi data.

4. Menentukan jumlah cluster.

5. Menghitung jarak Euclidean.

6. Update centroid.

7. Iterasi hingga cluster stabil.


## Evaluasi Hasil


Penjelasan algoritma digunakan sebagai dasar penyusunan bagian teknis proses clustering pada dokumen LLD.


---


# 8. Prompt Evaluasi Rancangan Sistem


## Tujuan

Melakukan pemeriksaan terhadap rancangan sistem agar lebih terstruktur.


## Prompt yang Digunakan


```
Lakukan evaluasi terhadap rancangan Sistem Klasterisasi Hafalan Santri dari sisi software architecture, database, API, dan keamanan sistem.
```


## Hasil dari AI


AI memberikan evaluasi berupa:


- Pemisahan modul sistem.
- Penggunaan arsitektur berlapis.
- Validasi data.
- Pengamanan autentikasi.
- Dokumentasi API.


## Evaluasi Hasil


Hasil evaluasi digunakan sebagai masukan untuk meningkatkan kualitas rancangan sistem.


---


# 9. Kesimpulan


AI digunakan sebagai alat bantu dalam proses perancangan Sistem Klasterisasi Hafalan Santri, terutama dalam penyusunan dokumen desain sistem, rancangan database, spesifikasi API, serta dokumentasi teknis.

Penggunaan AI mempercepat proses analisis dan dokumentasi, namun seluruh rancangan tetap melalui proses pemeriksaan dan penyesuaian agar sesuai dengan kebutuhan aplikasi yang dikembangkan.