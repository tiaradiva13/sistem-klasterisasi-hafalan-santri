# API Contract
# Sistem Klasterisasi Hafalan Santri


## Deskripsi

API Contract menjelaskan aturan komunikasi antara client dan server pada Sistem Klasterisasi Hafalan Santri.

Dokumen ini mendefinisikan struktur endpoint, format request, format response, aturan penamaan, dan standar penanganan error pada REST API.


# Base URL

```
http://localhost:8000/api
```


# Format Data

Seluruh komunikasi API menggunakan format JSON.

Header request:

```
Content-Type: application/json
```


# Endpoint API


# 1. Manajemen Data Santri


## GET /santri


### Deskripsi

Mengambil seluruh data santri yang tersimpan pada sistem.


### Method

```
GET
```


### Request

Tidak membutuhkan parameter.


### Response Success

Status:

```
200 OK
```


Response:

```json
[
  {
    "id_santri": 1,
    "nis": "2024001",
    "nama": "Ahmad Fauzi",
    "kelas": "3A",
    "jenis_kelamin": "L"
  }
]
```


## POST /santri


### Deskripsi

Menambahkan data santri baru.


### Method

```
POST
```


### Request Body

```json
{
  "nis": "2024002",
  "nama": "Muhammad Ali",
  "kelas": "3B",
  "jenis_kelamin": "L",
  "tanggal_lahir": "2010-01-10",
  "alamat": "Jakarta"
}
```


### Response Success

Status:

```
201 Created
```


Response:

```json
{
  "message": "Data santri berhasil ditambahkan",
  "id_santri": 2
}
```



# 2. Manajemen Data Hafalan


## POST /hafalan


### Deskripsi

Menyimpan data setoran hafalan santri.


### Method

```
POST
```


### Request Body

```json
{
  "id_santri": 1,
  "juz": 30,
  "surat": "An-Naba",
  "ayat_mulai": 1,
  "ayat_selesai": 40,
  "jumlah_ayat": 40,
  "tanggal_setoran": "2026-10-03",
  "nilai_hafalan": 90,
  "kualitas_bacaan": 85
}
```


### Response Success

Status:

```
201 Created
```


Response:

```json
{
  "message": "Data hafalan berhasil disimpan",
  "id_hafalan": 1
}
```



## GET /hafalan/{id_santri}


### Deskripsi

Mengambil seluruh riwayat hafalan berdasarkan santri.


### Parameter


| Parameter | Type | Keterangan |
|---|---|---|
| id_santri | Integer | ID santri |


### Response

Status:

```
200 OK
```


Response:

```json
[
  {
    "id_hafalan":1,
    "juz":30,
    "surat":"An-Naba",
    "nilai_hafalan":90
  }
]
```



# 3. Manajemen Evaluasi Hafalan


## POST /evaluasi


### Deskripsi

Menyimpan hasil evaluasi kualitas hafalan.


### Request Body

```json
{
  "id_hafalan":1,
  "kelancaran":90,
  "tajwid":85,
  "makhraj":88,
  "catatan":"Perlu peningkatan kelancaran",
  "tanggal_eval":"2026-10-03"
}
```


### Response Success

Status:

```
201 Created
```


Response:

```json
{
  "message":"Evaluasi berhasil disimpan",
  "id_evaluasi":1
}
```



# 4. Proses Klasterisasi


## POST /clustering


### Deskripsi

Melakukan proses pengelompokan santri berdasarkan kemampuan hafalan.


### Request Body

```json
{
  "jumlah_cluster":3
}
```


### Response Success

Status:

```
200 OK
```


Response:

```json
[
  {
    "id_santri":1,
    "cluster_id":1,
    "nama_cluster":"Tinggi",
    "nilai_akhir":90,
    "tanggal_proses":"2026-10-03"
  }
]
```



# Struktur Response Standar


Response berhasil:

```json
{
  "status":"success",
  "data":{}
}
```


Response gagal:

```json
{
  "status":"error",
  "message":"Pesan kesalahan"
}
```



# HTTP Status Code


| Status Code | Keterangan |
|---|---|
|200|Request berhasil|
|201|Data berhasil dibuat|
|400|Request tidak valid|
|404|Data tidak ditemukan|
|500|Kesalahan server|



# Validasi Data


Data santri wajib memiliki:

```
nis
nama
kelas
jenis_kelamin
```


Data hafalan wajib memiliki:

```
id_santri
juz
surat
nilai_hafalan
kualitas_bacaan
```


Data evaluasi wajib memiliki:

```
id_hafalan
kelancaran
tajwid
makhraj
```


# Aturan Keamanan


API harus melakukan validasi terhadap:

- input kosong
- tipe data tidak sesuai
- ID yang tidak tersedia
- akses endpoint yang tidak valid


# Konsistensi Dengan Database


Endpoint API menggunakan struktur data yang sesuai dengan ERD:


```
SANTRI

    |
    |
    v

HAFALAN

    |
    |
    v

EVALUASI


SANTRI

    |
    |
    v

HASIL_CLUSTER
```


# Kesimpulan


API Contract ini menjadi pedoman implementasi REST API Sistem Klasterisasi Hafalan Santri.

Dokumen ini memastikan endpoint, struktur data, dan komunikasi antara client dan server memiliki standar yang konsisten.