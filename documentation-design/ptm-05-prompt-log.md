# PTM-05 Prompt Log
# Dokumentasi Penggunaan dan Evaluasi Prompt AI

## Sistem Klasterisasi Hafalan Santri


## Deskripsi

Dokumen ini berisi dokumentasi penggunaan Artificial Intelligence (AI) dalam proses perancangan Sistem Klasterisasi Hafalan Santri.

AI digunakan sebagai alat bantu untuk menghasilkan ide awal, membantu penyusunan rancangan sistem, membuat struktur dokumentasi, serta melakukan evaluasi terhadap hasil desain.

Seluruh hasil dari AI dilakukan proses review dan validasi agar sesuai dengan kebutuhan sistem.


# Prompt 1

## Tujuan

Menganalisis kebutuhan sistem dan menentukan komponen utama Sistem Klasterisasi Hafalan Santri.


## Prompt yang Digunakan

```
Buatkan analisis kebutuhan sistem untuk aplikasi
klasterisasi hafalan santri yang dapat mengelompokkan
santri berdasarkan kemampuan hafalan.
```


## Hasil AI

AI memberikan rancangan kebutuhan sistem yang terdiri dari:

- Data santri
- Data hafalan
- Data evaluasi
- Proses clustering
- Hasil pengelompokan kemampuan santri


## Evaluasi Hasil

Hasil AI telah sesuai dengan konsep awal sistem, namun perlu penyesuaian pada struktur data agar sesuai dengan kebutuhan database.


## Perbaikan

Menambahkan komponen:

- atribut kualitas bacaan
- nilai hafalan
- histori proses clustering



# Prompt 2

## Tujuan

Membuat rancangan Entity Relationship Diagram (ERD).


## Prompt yang Digunakan

```
Buatkan rancangan ERD untuk sistem klasterisasi
hafalan santri yang memiliki data santri,
hafalan, evaluasi, dan hasil clustering.
```


## Hasil AI

AI menghasilkan rancangan entity:

- SANTRI
- HAFALAN
- EVALUASI
- HASIL_CLUSTER


## Evaluasi Hasil

Struktur entity sudah sesuai, tetapi dilakukan pengecekan kembali terhadap:

- primary key
- foreign key
- hubungan antar tabel
- kebutuhan atribut


## Perbaikan

Relasi akhir yang digunakan:

```
SANTRI
 |
 | 1:N
 |
HAFALAN
 |
 | 1:N
 |
EVALUASI


SANTRI
 |
 | 1:N
 |
HASIL_CLUSTER
```



# Prompt 3

## Tujuan

Membuat rancangan REST API.


## Prompt yang Digunakan

```
Buatkan desain REST API untuk sistem
klasterisasi hafalan santri.
Berikan endpoint, request, response,
dan status code.
```


## Hasil AI

AI menghasilkan rancangan endpoint:

```
GET /santri

POST /santri

POST /hafalan

GET /hafalan/{id_santri}

POST /evaluasi

POST /clustering
```


## Evaluasi Hasil

Endpoint telah sesuai dengan fungsi utama sistem.

Dilakukan validasi terhadap:

- kesesuaian endpoint dengan database
- format request
- format response
- penggunaan HTTP method


## Perbaikan

Menyesuaikan struktur response dengan model data Pydantic.


# Prompt 4

## Tujuan

Membuat model data menggunakan Pydantic.


## Prompt yang Digunakan

```
Buatkan schema model Pydantic berdasarkan
database sistem klasterisasi hafalan santri.
```


## Hasil AI

AI menghasilkan model:

```
Santri

Hafalan

Evaluasi

HasilCluster
```


## Evaluasi Hasil

Model diperiksa berdasarkan ERD agar seluruh atribut memiliki hubungan yang benar.


## Perbaikan

Menambahkan:

- Foreign Key
- atribut tanggal
- atribut nilai
- validasi tipe data



# Validasi Akhir


Seluruh hasil rancangan AI dibandingkan dengan kebutuhan sistem.

Validasi dilakukan pada:

| Komponen | Status |
|---|---|
| ERD | Sesuai |
| Model Data | Sesuai |
| API Contract | Sesuai |
| OpenAPI Specification | Sesuai |
| Struktur Database | Sesuai |


# Kesimpulan


AI digunakan sebagai pendukung proses perancangan sistem, bukan sebagai pengganti proses analisis.

Setiap hasil yang diberikan AI dilakukan pemeriksaan ulang dan penyesuaian berdasarkan kebutuhan Sistem Klasterisasi Hafalan Santri.

Dokumentasi ini menunjukkan proses penggunaan AI secara transparan mulai dari pembuatan rancangan awal sampai validasi hasil akhir.