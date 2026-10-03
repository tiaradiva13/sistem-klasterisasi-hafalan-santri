# Low-Level Design (LLD) Awal
# Sistem Klasterisasi Hafalan Santri


## 1. Pendahuluan

Low-Level Design (LLD) merupakan dokumen rancangan teknis yang menjelaskan detail implementasi sistem berdasarkan rancangan High-Level Design (HLD).

Dokumen ini berisi rancangan struktur database, desain modul, spesifikasi API, struktur folder aplikasi, alur proses sistem, mekanisme algoritma clustering, serta rancangan pengujian sistem.

Sistem Klasterisasi Hafalan Santri dikembangkan untuk membantu proses pengelolaan data hafalan santri dan melakukan analisis pengelompokan berdasarkan pola perkembangan hafalan menggunakan metode clustering.


---

# 2. Desain Database


Database digunakan untuk menyimpan seluruh data yang digunakan dalam sistem, meliputi data pengguna, data santri, data hafalan, dan hasil proses clustering.


## 2.1 Relasi Antar Entitas


```
Users
 |
 |
Santri
 |
 |
Hafalan
 |
 |
Cluster Result
```


Penjelasan:

- Users menyimpan data pengguna yang memiliki akses ke sistem.
- Santri menyimpan informasi identitas santri.
- Hafalan menyimpan data perkembangan hafalan santri.
- Cluster Result menyimpan hasil pengelompokan santri berdasarkan algoritma clustering.


---

# 3. Struktur Tabel Database


## 3.1 Tabel Users

Tabel users digunakan untuk menyimpan informasi akun pengguna.


| Field | Tipe Data | Keterangan |
|---|---|---|
| id_user | Integer | Primary Key |
| username | Varchar | Nama pengguna |
| password | Varchar | Password terenkripsi |
| role | Varchar | Hak akses pengguna |
| created_at | Timestamp | Waktu pembuatan data |


Role pengguna:

- Admin
- Ustadz


---

## 3.2 Tabel Santri

Tabel santri menyimpan data identitas santri.


| Field | Tipe Data | Keterangan |
|---|---|---|
| id_santri | Integer | Primary Key |
| nama_santri | Varchar | Nama lengkap santri |
| jenis_kelamin | Varchar | Jenis kelamin |
| tanggal_lahir | Date | Tanggal lahir |
| kelas | Varchar | Tingkatan kelas |
| alamat | Text | Alamat santri |


Relasi:

```
Users (1) -------- (N) Santri
```


---

## 3.3 Tabel Hafalan

Tabel hafalan digunakan untuk menyimpan perkembangan hafalan santri.


| Field | Tipe Data | Keterangan |
|---|---|---|
| id_hafalan | Integer | Primary Key |
| id_santri | Integer | Foreign Key |
| jumlah_juz | Float | Jumlah hafalan |
| jumlah_setoran | Integer | Jumlah setoran |
| nilai_hafalan | Float | Nilai evaluasi |
| tanggal_setoran | Date | Tanggal setoran |


Relasi:

```
Santri (1) -------- (N) Hafalan
```


---

## 3.4 Tabel Cluster Result

Tabel cluster result menyimpan hasil pengelompokan santri.


| Field | Tipe Data | Keterangan |
|---|---|---|
| id_cluster | Integer | Primary Key |
| id_santri | Integer | Foreign Key |
| cluster_label | Varchar | Label kelompok |
| nilai_cluster | Float | Nilai hasil clustering |
| created_at | Timestamp | Waktu proses |


Contoh hasil:

```
Cluster 1 : Hafalan Tinggi

Cluster 2 : Hafalan Sedang

Cluster 3 : Hafalan Rendah
```


---

# 4. Desain Modul Sistem


## 4.1 Modul Authentication


Modul authentication digunakan untuk mengatur proses login dan keamanan akses pengguna.


Fungsi:

- Login pengguna.
- Logout pengguna.
- Validasi akun.
- Pengaturan hak akses.


Input:

```
username
password
```


Output:

```
status login
role pengguna
token akses
```


---

## 4.2 Modul Manajemen Data Santri


Modul ini digunakan untuk mengelola informasi santri.


Fitur:

- Menampilkan data santri.
- Menambahkan data santri.
- Mengubah data santri.
- Menghapus data santri.


Alur proses:


```
Input Data Santri

        |

Validasi Data

        |

Simpan Database

        |

Data Santri Tersimpan
```


---

## 4.3 Modul Manajemen Hafalan


Modul ini digunakan untuk mencatat perkembangan hafalan.


Data yang dikelola:

- Jumlah juz hafalan.
- Jumlah setoran.
- Nilai evaluasi.
- Tanggal setoran.


Alur proses:


```
Input Hafalan

        |

Validasi Data

        |

Penyimpanan Database

        |

Update Perkembangan Hafalan
```


---

## 4.4 Modul Klasterisasi


Modul klasterisasi merupakan modul utama dalam sistem yang digunakan untuk mengelompokkan santri berdasarkan kemiripan data hafalan.


Input:

```
jumlah_juz
jumlah_setoran
nilai_hafalan
```


Output:

```
kelompok santri
hasil cluster
```


Proses:

1. Mengambil data hafalan dari database.
2. Melakukan preprocessing data.
3. Melakukan normalisasi data.
4. Menjalankan algoritma K-Means.
5. Menyimpan hasil clustering.


---

## 4.5 Modul Dashboard


Modul dashboard digunakan untuk menampilkan hasil analisis sistem.


Fitur:

- Statistik jumlah santri.
- Grafik perkembangan hafalan.
- Visualisasi hasil clustering.
- Informasi karakteristik kelompok.


---

# 5. Detail Algoritma K-Means Clustering


Algoritma K-Means digunakan untuk mengelompokkan santri berdasarkan tingkat perkembangan hafalan.


## 5.1 Input Data


Variabel yang digunakan:

```
X = {
jumlah_hafalan,
jumlah_setoran,
nilai_hafalan
}
```


---

## 5.2 Normalisasi Data


Normalisasi digunakan untuk menyamakan skala setiap variabel.


Rumus:

```
X' = (X - Xmin) / (Xmax - Xmin)
```


---

## 5.3 Menentukan Jumlah Cluster


Jumlah cluster ditentukan berdasarkan kebutuhan analisis.


Contoh:

```
K = 3
```


Kategori:

```
Cluster 1 = Hafalan Tinggi

Cluster 2 = Hafalan Sedang

Cluster 3 = Hafalan Rendah
```


---

## 5.4 Menghitung Jarak Data


Metode perhitungan menggunakan Euclidean Distance.


Rumus:

```
d(x,y)=√((x1-y1)²+(x2-y2)²+...+(xn-yn)²)
```


---

## 5.5 Update Centroid


Centroid diperbarui berdasarkan nilai rata-rata setiap anggota cluster.


---

## 5.6 Iterasi


Proses dilakukan secara berulang sampai:

- Posisi centroid stabil.
- Tidak terjadi perubahan anggota cluster.


---

# 6. Spesifikasi API


API digunakan sebagai penghubung komunikasi antara frontend, backend, dan database.


Format:

```
REST API
JSON Response
```


---

# 6.1 Authentication API


## POST /api/login


Fungsi:

Melakukan autentikasi pengguna.


Request:


```json
{
 "username": "admin",
 "password": "123456"
}
```


Response:


```json
{
 "status": "success",
 "token": "xxxxx",
 "role": "admin"
}
```


---

# 6.2 Data Santri API


## GET /api/santri


Fungsi:

Mengambil daftar data santri.


Response:


```json
[
 {
  "id":1,
  "nama":"Ahmad",
  "kelas":"Tahfidz A"
 }
]
```


---

## POST /api/santri


Fungsi:

Menambahkan data santri.


Request:


```json
{
 "nama":"Ahmad",
 "kelas":"Tahfidz A"
}
```


---

## PUT /api/santri/{id}


Fungsi:

Mengubah data santri.


---

## DELETE /api/santri/{id}


Fungsi:

Menghapus data santri.


---

# 6.3 Data Hafalan API


## POST /api/hafalan


Request:


```json
{
"id_santri":1,
"jumlah_juz":5,
"jumlah_setoran":20,
"nilai_hafalan":85
}
```


Response:


```json
{
"status":"success",
"message":"Data hafalan berhasil disimpan"
}
```


---

# 6.4 Clustering API


## POST /api/clustering


Fungsi:

Menjalankan proses klasterisasi.


Request:


```json
{
"jumlah_cluster":3
}
```


Response:


```json
{
"cluster_1":"Hafalan Tinggi",
"cluster_2":"Hafalan Sedang",
"cluster_3":"Hafalan Rendah"
}
```


---

# 7. Struktur Folder Aplikasi


```
sistem-klasterisasi-hafalan-santri

|

|-- frontend

|   |-- pages

|   |-- components

|   |-- assets


|

|-- backend

|   |-- controllers

|   |-- models

|   |-- routes

|   |-- services

|   |-- algorithms


|

|-- database

|   |-- migration

|   |-- seed


|

|-- documentation

    |-- hld.md

    |-- lld-awal.md

    |-- prompt-log.md
```


---

# 8. Alur Proses Sistem


## 8.1 Proses Input Data Hafalan


```
Ustadz Login

        |

Input Hafalan Santri

        |

Validasi Data

        |

Simpan Database

        |

Data Siap Diproses
```


---

## 8.2 Proses Clustering


```
Ambil Data Hafalan

        |

Preprocessing Data

        |

Normalisasi Data

        |

K-Means Algorithm

        |

Hasil Cluster

        |

Simpan Hasil

        |

Dashboard
```


---

# 9. Rancangan Pengujian Sistem


## 9.1 Functional Testing


Pengujian fungsi utama:


| Fitur | Pengujian |
|---|---|
| Login | Validasi akun pengguna |
| Data Santri | CRUD data santri |
| Data Hafalan | Input dan penyimpanan |
| Clustering | Proses pengelompokan |
| Dashboard | Tampilan hasil analisis |


---

## 9.2 Performance Testing


Parameter pengujian:

- Waktu proses clustering.
- Kecepatan respon API.
- Jumlah data yang mampu diproses.
- Stabilitas sistem saat digunakan.


---

# 10. Kesimpulan


Low-Level Design (LLD) Awal Sistem Klasterisasi Hafalan Santri menjelaskan rancangan teknis sistem secara detail mulai dari struktur database, desain modul, algoritma clustering, spesifikasi API, struktur folder aplikasi, hingga rancangan pengujian.

Dokumen ini menjadi dasar implementasi sistem agar proses pengembangan aplikasi berjalan secara sistematis, terstruktur, dan sesuai dengan rancangan High-Level Design (HLD).