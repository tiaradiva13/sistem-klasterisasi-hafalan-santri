# High-Level Design (HLD)
# Sistem Klasterisasi Hafalan Santri


## 1. Pendahuluan

### 1.1 Deskripsi Sistem

Sistem Klasterisasi Hafalan Santri merupakan aplikasi berbasis teknologi informasi yang dirancang untuk membantu pihak pesantren dalam mengelola, memantau, dan menganalisis perkembangan hafalan santri secara digital.

Aplikasi ini menggunakan pendekatan data mining dengan metode clustering untuk mengelompokkan santri berdasarkan pola perkembangan hafalan. Proses pengelompokan dilakukan berdasarkan beberapa parameter seperti jumlah hafalan, jumlah setoran, nilai evaluasi, serta tingkat konsistensi perkembangan hafalan.

Hasil dari proses klasterisasi dapat digunakan oleh ustadz atau pengelola pesantren sebagai pendukung pengambilan keputusan dalam memberikan strategi pembinaan hafalan yang lebih sesuai berdasarkan karakteristik masing-masing kelompok santri.


## 2. Tujuan Sistem

Tujuan pengembangan Sistem Klasterisasi Hafalan Santri adalah:

1. Membantu proses pengelolaan data santri secara digital dan terstruktur.

2. Membantu pencatatan perkembangan hafalan santri.

3. Mengolah data hafalan menggunakan metode clustering untuk menemukan pola kemampuan santri.

4. Menghasilkan informasi kelompok santri berdasarkan tingkat perkembangan hafalan.

5. Membantu ustadz dalam melakukan evaluasi dan menentukan strategi pembinaan hafalan.


## 3. Ruang Lingkup Sistem

Sistem memiliki beberapa ruang lingkup utama sebagai berikut:

### 3.1 Pengelolaan Data Santri

Sistem menyediakan fitur untuk:

- Menambahkan data santri.
- Mengubah data santri.
- Menghapus data santri.
- Melihat informasi santri.


### 3.2 Pengelolaan Data Hafalan

Sistem dapat melakukan:

- Input jumlah hafalan santri.
- Menyimpan riwayat setoran hafalan.
- Menyimpan nilai evaluasi hafalan.
- Melakukan pemantauan perkembangan hafalan.


### 3.3 Proses Klasterisasi

Sistem melakukan proses analisis data dengan tahapan:

- Pengumpulan data hafalan.
- Preprocessing data.
- Perhitungan algoritma clustering.
- Pembentukan kelompok santri.


### 3.4 Penyajian Informasi

Sistem menyediakan informasi berupa:

- Dashboard perkembangan hafalan.
- Statistik hafalan santri.
- Hasil pengelompokan cluster.
- Informasi karakteristik setiap kelompok.


## 4. Aktor Sistem

Sistem memiliki beberapa aktor yang berinteraksi dengan aplikasi.


### 4.1 Admin

Admin merupakan pengguna yang bertanggung jawab dalam pengelolaan sistem.

Hak akses:

- Melakukan login.
- Mengelola akun pengguna.
- Mengelola data santri.
- Mengelola data hafalan.
- Melihat laporan hasil sistem.


### 4.2 Ustadz

Ustadz merupakan pengguna yang bertanggung jawab dalam melakukan monitoring perkembangan hafalan.

Hak akses:

- Melakukan login.
- Input perkembangan hafalan.
- Melihat data santri.
- Melihat hasil klasterisasi.


### 4.3 Sistem

Sistem bertugas melakukan proses otomatis seperti:

- Penyimpanan data.
- Pengolahan data.
- Perhitungan algoritma clustering.
- Penyajian hasil analisis.


## 5. Arsitektur Sistem

Sistem menggunakan konsep arsitektur tiga lapisan (Three-Tier Architecture), yaitu Presentation Layer, Application Layer, dan Data Layer.


```
+--------------------------------+
|       Presentation Layer       |
|                                |
|  Web Interface                 |
|  Dashboard                     |
|  Form Input Data               |
|  Visualisasi Hasil             |
+---------------+----------------+
                |
                |
                v
+--------------------------------+
|       Application Layer        |
|                                |
|  Backend API                   |
|  Business Logic                |
|  Authentication Service        |
|  Clustering Service            |
+---------------+----------------+
                |
                |
                v
+--------------------------------+
|          Data Layer            |
|                                |
|  Database                     |
|  Data Santri                  |
|  Data Hafalan                 |
|  Data Cluster                 |
+--------------------------------+
```


### 5.1 Presentation Layer

Presentation Layer merupakan bagian sistem yang berinteraksi langsung dengan pengguna.

Fungsi:

- Menampilkan halaman aplikasi.
- Menyediakan form input data.
- Menampilkan hasil analisis.
- Menampilkan dashboard.


### 5.2 Application Layer

Application Layer berfungsi menjalankan proses bisnis aplikasi.

Fungsi:

- Mengelola autentikasi pengguna.
- Melakukan validasi data.
- Menghubungkan frontend dengan database.
- Menjalankan proses clustering.


### 5.3 Data Layer

Data Layer berfungsi sebagai tempat penyimpanan data sistem.

Data yang disimpan:

- Data pengguna.
- Data santri.
- Data hafalan.
- Data hasil clustering.


## 6. Diagram Alur Data Sistem


```
User
 |
 |
Input Data Santri dan Hafalan
 |
 |
Database
 |
 |
Preprocessing Data
 |
 |
Algoritma K-Means Clustering
 |
 |
Hasil Pengelompokan Santri
 |
 |
Dashboard Sistem
 |
 |
Informasi Cluster
```


Alur proses sistem:

1. Pengguna memasukkan data santri dan perkembangan hafalan.

2. Data disimpan ke dalam database.

3. Sistem melakukan preprocessing terhadap data yang akan dianalisis.

4. Data diproses menggunakan algoritma clustering.

5. Sistem menghasilkan kelompok santri berdasarkan karakteristik hafalan.

6. Hasil ditampilkan melalui dashboard.


## 7. Desain Modul Sistem


### 7.1 Modul Authentication

Modul Authentication digunakan untuk mengatur proses akses pengguna.

Fitur:

- Login pengguna.
- Logout pengguna.
- Pengaturan hak akses.


Input:

- Username.
- Password.


Output:

- Status login.
- Informasi role pengguna.


### 7.2 Modul Manajemen Data Santri

Modul ini digunakan untuk mengelola informasi santri.

Fitur:

- Tambah data santri.
- Edit data santri.
- Hapus data santri.
- Melihat daftar santri.


### 7.3 Modul Manajemen Hafalan

Modul ini digunakan untuk mencatat perkembangan hafalan.

Fitur:

- Input jumlah hafalan.
- Input nilai hafalan.
- Menyimpan riwayat setoran.
- Monitoring perkembangan.


### 7.4 Modul Klasterisasi

Modul klasterisasi merupakan modul utama dalam sistem.

Fungsi:

- Mengambil data hafalan.
- Melakukan preprocessing.
- Menjalankan algoritma K-Means.
- Menghasilkan kelompok santri.


Tahapan proses:

1. Menentukan dataset.

2. Melakukan normalisasi data.

3. Menentukan jumlah cluster.

4. Menghitung jarak data terhadap centroid.

5. Melakukan pengelompokan data.

6. Menghasilkan hasil cluster.


### 7.5 Modul Dashboard

Modul dashboard berfungsi memberikan informasi hasil sistem.

Fitur:

- Statistik jumlah santri.
- Grafik perkembangan hafalan.
- Visualisasi hasil clustering.
- Informasi kelompok santri.


## 8. Teknologi Sistem

Teknologi yang digunakan dalam pengembangan sistem terdiri dari:


### Frontend

Digunakan untuk membangun antarmuka pengguna.

Komponen:

- HTML.
- CSS.
- JavaScript.


### Backend

Digunakan untuk menjalankan logika sistem.

Komponen:

- Backend Framework.
- REST API.
- Business Logic.


### Database

Digunakan untuk penyimpanan data.

Komponen:

- MySQL/PostgreSQL.


### Machine Learning

Digunakan untuk proses analisis data.

Metode:

- K-Means Clustering.


## 9. Keamanan Sistem

Sistem menerapkan beberapa mekanisme keamanan:


### Authentication

Pengguna harus melakukan login sebelum menggunakan sistem.


### Authorization

Hak akses pengguna dibatasi berdasarkan peran pengguna.


### Validasi Input

Setiap data yang masuk akan melalui proses validasi untuk menjaga kualitas data.


### Perlindungan Password

Password pengguna disimpan menggunakan metode hashing.


## 10. Deployment Architecture


```
Client Browser

      |

      |

Web Server

      |

      |

Application Server

      |

      |

Database Server
```


Komponen deployment:

1. Client mengakses aplikasi melalui browser.

2. Web server menerima permintaan pengguna.

3. Application server menjalankan proses aplikasi.

4. Database server menyimpan seluruh data sistem.


## 11. Kesimpulan

High-Level Design Sistem Klasterisasi Hafalan Santri memberikan gambaran umum mengenai struktur sistem, arsitektur aplikasi, hubungan antar komponen, aliran data, serta modul utama yang digunakan.

Dokumen HLD ini menjadi dasar untuk tahap perancangan berikutnya yaitu Low-Level Design (LLD), implementasi sistem, serta proses pengujian aplikasi.