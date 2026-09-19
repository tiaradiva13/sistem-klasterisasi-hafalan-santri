# User Stories
## Sistem Analisis Komparatif K-Means dan K-Medoids untuk Klasterisasi Pola Hafalan Santri

---

## 1. Informasi Proyek

**Nama Sistem**  
Sistem Analisis Pola Hafalan Santri Menggunakan Algoritma K-Means dan K-Medoids

**Deskripsi Sistem**  
Sistem ini merupakan aplikasi berbasis web yang digunakan untuk melakukan analisis pola hafalan santri berdasarkan data setoran dan murojaah. Sistem menerapkan metode clustering K-Means dan K-Medoids untuk mengelompokkan santri berdasarkan karakteristik aktivitas hafalan.

**Tujuan Sistem**

1. Membantu pembina tahfidz mengetahui pola hafalan santri.
2. Mengelompokkan santri berdasarkan karakteristik setoran dan murojaah.
3. Membantu menentukan strategi pembinaan berdasarkan hasil clustering.
4. Membandingkan performa algoritma K-Means dan K-Medoids dalam melakukan pengelompokan.


**Platform**
- Website

**Fitur AI**
- Klasterisasi pola hafalan menggunakan algoritma K-Means.
- Klasterisasi pola hafalan menggunakan algoritma K-Medoids.
- Perbandingan hasil clustering menggunakan evaluasi model.

---

# 2. Persona Pengguna


## Persona 1: Admin Tahfidz

**Peran:**  
Mengelola data santri dan memastikan data sistem tersedia.

**Permasalahan:**
- Data santri masih tersimpan secara manual.
- Kesulitan melakukan pengelolaan data dalam jumlah banyak.

**Kebutuhan:**
- Mengelola data santri.
- Melihat laporan hasil analisis.


---

## Persona 2: Pembina Tahfidz

**Peran:**  
Mengawasi perkembangan hafalan santri.

**Permasalahan:**
- Sulit mengetahui pola hafalan seluruh santri.
- Kesulitan menentukan santri yang membutuhkan pembinaan khusus.

**Kebutuhan:**
- Melakukan analisis pola hafalan.
- Melihat hasil pengelompokan santri.
- Membandingkan hasil algoritma clustering.


---

# 3. Functional Requirement (FR)


## FR-01 Login Sistem

Sistem menyediakan fitur autentikasi pengguna agar admin dan pembina dapat mengakses sistem sesuai hak akses.


---

## FR-02 Pengelolaan Data Santri

Sistem menyediakan fitur pengelolaan data santri yang meliputi:

- Menambahkan data santri.
- Mengubah data santri.
- Menghapus data santri.
- Melihat daftar santri.


Data santri:

- ID Santri
- Nama Santri
- Kelas


---

## FR-03 Pengelolaan Data Hafalan

Sistem menyediakan fitur input data perkembangan hafalan santri.

Data yang digunakan:

- Jumlah setoran hafalan.
- Jumlah murojaah.
- Frekuensi hafalan.
- Nilai kelancaran.


---

## FR-04 Klasterisasi Menggunakan K-Means ★

Sistem melakukan proses clustering menggunakan algoritma K-Means berdasarkan data hafalan santri.

Input:

- Dataset hafalan santri.

Output:

- Kelompok cluster pola hafalan.


---

## FR-05 Klasterisasi Menggunakan K-Medoids ★

Sistem melakukan proses clustering menggunakan algoritma K-Medoids berdasarkan data hafalan santri.

Input:

- Dataset hafalan santri.

Output:

- Kelompok cluster pola hafalan.


---

## FR-06 Perbandingan Hasil Algoritma ★

Sistem menyediakan fitur perbandingan hasil K-Means dan K-Medoids.

Parameter perbandingan:

- Hasil cluster.
- Nilai evaluasi clustering.
- Karakteristik setiap kelompok.


---

## FR-07 Visualisasi Hasil Analisis

Sistem menampilkan hasil analisis dalam bentuk:

- Tabel hasil cluster.
- Grafik visualisasi.
- Laporan analisis.


---

# 4. Non Functional Requirement (NFR)


## NFR-01

Sistem dapat berjalan menggunakan browser.


## NFR-02

Sistem mampu memberikan respon proses analisis maksimal 5 detik untuk dataset normal.


## NFR-03

Data pengguna dan data santri tersimpan secara aman.


---

# 5. User Story


## US-01 Login Sistem

**Narasi:**

Sebagai admin tahfidz, saya ingin melakukan login ke sistem, agar saya dapat mengakses fitur pengelolaan data santri.

**FR Asal:**  
FR-01

**Prioritas:**  
Must

**Kategori:**  
Fitur Inti


---

## US-02 Mengelola Data Santri

**Narasi:**

Sebagai admin tahfidz, saya ingin mengelola data santri, agar informasi santri dapat tersimpan secara terstruktur.

**FR Asal:**  
FR-02

**Prioritas:**  
Must

**Kategori:**  
Fitur Inti


---

## US-03 Menginput Data Hafalan

**Narasi:**

Sebagai pembina tahfidz, saya ingin memasukkan data setoran dan murojaah santri, agar sistem memiliki data untuk melakukan analisis pola hafalan.

**FR Asal:**  
FR-03

**Prioritas:**  
Must

**Kategori:**  
Fitur Inti


---

## US-04 Melakukan Klasterisasi K-Means ★

**Narasi:**

Sebagai pembina tahfidz, saya ingin melakukan analisis clustering menggunakan algoritma K-Means, agar saya dapat mengetahui kelompok pola hafalan santri.

**FR Asal:**  
FR-04

**Prioritas:**  
Should

**Kategori:**  
Fitur AI


---

## US-05 Melakukan Klasterisasi K-Medoids ★

**Narasi:**

Sebagai pembina tahfidz, saya ingin melakukan analisis clustering menggunakan algoritma K-Medoids, agar saya dapat membandingkan hasil pengelompokan dengan metode lain.

**FR Asal:**  
FR-05

**Prioritas:**  
Should

**Kategori:**  
Fitur AI


---

## US-06 Membandingkan Hasil Clustering ★

**Narasi:**

Sebagai pembina tahfidz, saya ingin melihat perbandingan hasil K-Means dan K-Medoids, agar saya dapat mengetahui karakteristik hasil clustering yang diperoleh.

**FR Asal:**  
FR-06

**Prioritas:**  
Should

**Kategori:**  
Fitur AI


---

## US-07 Melihat Visualisasi Hasil Analisis

**Narasi:**

Sebagai pembina tahfidz, saya ingin melihat visualisasi hasil clustering, agar saya lebih mudah memahami pola hafalan santri.

**FR Asal:**  
FR-07

**Prioritas:**  
Should

**Kategori:**  
Fitur Inti


---

# 6. Evaluasi Prinsip INVEST


|ID|Independent|Negotiable|Valuable|Estimable|Small|Testable|
|-|-|-|-|-|-|-|
|US-01|✓|✓|✓|✓|✓|✓|
|US-02|✓|✓|✓|✓|✓|✓|
|US-03|✓|✓|✓|✓|✓|✓|
|US-04|✓|✓|✓|✓|✓|✓|
|US-05|✓|✓|✓|✓|✓|✓|
|US-06|✓|✓|✓|✓|✓|✓|
|US-07|✓|✓|✓|✓|✓|✓|

---

# 7. Use Case


# UC-01 Analisis Klasterisasi Pola Hafalan


## Aktor Utama

Pembina Tahfidz


## Aktor Pendukung

- Database
- Machine Learning Service


## Precondition

- Pembina sudah login.
- Dataset hafalan santri tersedia.


## Postcondition

- Sistem menghasilkan kelompok pola hafalan santri.
- Sistem menampilkan hasil clustering.


---

## Alur Utama

1. Pembina membuka menu analisis hafalan.
2. Pembina memilih dataset santri.
3. Sistem melakukan validasi data.
4. Sistem melakukan preprocessing data.
5. Sistem menjalankan algoritma K-Means.
6. Sistem menjalankan algoritma K-Medoids.
7. Sistem menghitung nilai evaluasi.
8. Sistem menampilkan hasil clustering.


---

## Alur Alternatif

Jika data tidak lengkap:

1. Sistem mendeteksi data kosong.
2. Sistem menampilkan informasi data belum lengkap.
3. Pembina memperbaiki data.


---

## Alur Eksepsi AI


### Data Input Tidak Valid

Sistem menolak proses analisis dan meminta pengguna memperbaiki dataset.


### Proses Clustering Gagal

Sistem menampilkan pesan bahwa proses analisis tidak dapat dilakukan.


### Hasil Analisis Tidak Stabil

Sistem memberikan informasi bahwa parameter clustering perlu dievaluasi kembali.


---

# 8. User Flow


```mermaid
flowchart TD

A[Login Sistem]

B[Menu Analisis Hafalan]

C[Pilih Dataset Santri]

D{Validasi Data}

E[Preprocessing Dataset]

F[Proses K-Means]

G[Proses K-Medoids]

H[Evaluasi Hasil]

I[Tampilkan Cluster]

J[Simpan Laporan]


A --> B
B --> C
C --> D

D -->|Tidak Valid| C

D -->|Valid| E

E --> F
F --> G
G --> H
H --> I
I --> J