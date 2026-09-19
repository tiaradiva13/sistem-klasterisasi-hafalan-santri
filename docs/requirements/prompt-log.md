# Prompt Log

## Project Information

**Nama Proyek**

Analisis Komparatif K-Means dan K-Medoids untuk Klasterisasi Pola Hafalan Santri Berdasarkan Data Setoran dan Murojaah


**Dokumen**

Prompt Log Pertemuan 03  
SRS → User Story → Use Case → User Flow → Acceptance Criteria


**Tujuan**

Dokumen ini berisi catatan penggunaan AI dalam proses penyusunan kebutuhan perangkat lunak, mulai dari prompt yang diberikan, hasil generate awal AI, hingga koreksi manual yang dilakukan oleh tim.


---

# 1. Prompt Tahap 1 — Penyusunan User Story


## Role

Kamu adalah Agile Product Owner dan Business Analyst.


## Task

Ubah daftar Functional Requirement (FR) dari SRS menjadi draft User Story menggunakan prinsip INVEST.


## Context

### Nama Sistem

Sistem Analisis Komparatif K-Means dan K-Medoids untuk Klasterisasi Pola Hafalan Santri.


### Platform

Website


### Persona Pengguna

1. Admin Tahfidz

Tugas:
- Mengelola data santri.
- Mengelola data sistem.
- Melihat laporan analisis.


2. Pembina Tahfidz

Tugas:
- Menginput data hafalan.
- Melakukan analisis pola hafalan.
- Mengevaluasi hasil clustering.


### Fitur AI

Fitur AI yang digunakan:

- Algoritma K-Means untuk clustering pola hafalan.
- Algoritma K-Medoids untuk clustering pola hafalan.
- Perbandingan hasil clustering.


### Functional Requirement

FR-01:
Login Sistem.

FR-02:
Pengelolaan Data Santri.

FR-03:
Pengelolaan Data Hafalan.

FR-04:
Clustering Menggunakan K-Means.

FR-05:
Clustering Menggunakan K-Medoids.

FR-06:
Perbandingan Hasil Algoritma.

FR-07:
Visualisasi Hasil Analisis.


## Output yang Diminta

Buat:

1. ID User Story.
2. Narasi user story dengan format:

"Sebagai <peran>, saya ingin <kemampuan>, agar <manfaat>."

3. FR asal.
4. Prioritas MoSCoW.
5. Kategori fitur.


---

# 2. Draft Awal Hasil Generate AI


Berdasarkan prompt tahap pertama, AI menghasilkan beberapa user story awal:


## US-01 Login Sistem

Sebagai pengguna, saya ingin login ke sistem agar dapat menggunakan aplikasi.


## US-02 Mengelola Data Santri

Sebagai pengguna, saya ingin mengelola data santri agar data tersimpan.


## US-03 Melakukan Analisis Hafalan

Sebagai pengguna, saya ingin melakukan analisis hafalan menggunakan AI agar mengetahui pola hafalan.


## US-04 Membandingkan Algoritma

Sebagai pengguna, saya ingin membandingkan algoritma agar mengetahui hasil terbaik.


---

# 3. Koreksi Manual User Story


## Koreksi 1: Penyesuaian Aktor Pengguna


### Hasil AI Awal:

"Sebagai pengguna"


### Perbaikan:

Aktor harus berdasarkan persona nyata.

Perubahan:

- Pengguna → Admin Tahfidz
- Pengguna → Pembina Tahfidz


Alasan:

User story harus menggambarkan kebutuhan aktor sebenarnya.


---

## Koreksi 2: Pemisahan Fitur AI


### Hasil AI Awal:

Analisis hafalan menggunakan AI dibuat menjadi satu user story besar.


### Perbaikan:

Dipecah menjadi:

- US-04 Analisis K-Means.
- US-05 Analisis K-Medoids.
- US-06 Perbandingan hasil algoritma.


Alasan:

Memenuhi prinsip INVEST, terutama aspek Small dan Testable.


---

## Koreksi 3: Penambahan Kategori Fitur


Setiap user story diberi kategori:

- Fitur Inti.
- Fitur AI.


Tujuan:

Memisahkan kebutuhan sistem umum dengan fitur machine learning.


---

# 4. Prompt Tahap 2 — Penyusunan Use Case


## Role

Kamu adalah System Analyst aplikasi cerdas.


## Task

Buat Use Case formal berdasarkan User Story fitur AI.


## Context

Fitur AI:

Klasterisasi pola hafalan santri menggunakan:

- K-Means.
- K-Medoids.


Input:

- Data setoran hafalan.
- Data murojaah.
- Data konsistensi.
- Nilai kelancaran.


Aktor:

Pembina Tahfidz.


## Output

Buat:

- ID Use Case.
- Nama Use Case.
- Aktor utama.
- Aktor pendukung.
- Precondition.
- Postcondition.
- Alur utama.
- Alur alternatif.
- Skenario kegagalan AI.


---

# 5. Draft Awal Hasil Generate Use Case


AI menghasilkan Use Case:

UC-01 Analisis Klasterisasi Pola Hafalan.


Alur utama:

1. Pembina memilih data santri.
2. Sistem melakukan preprocessing.
3. Sistem menjalankan algoritma.
4. Sistem menampilkan hasil.


---

# 6. Koreksi Manual Use Case


Penambahan skenario khusus AI:


## Data Input Tidak Valid

Tambahan:

Sistem harus memberikan notifikasi ketika dataset tidak lengkap.


## Kegagalan Proses

Tambahan:

Sistem harus menangani kegagalan proses clustering.


## Hasil Tidak Stabil

Tambahan:

Sistem memberikan informasi bahwa parameter analisis perlu dievaluasi.


---

# 7. Prompt Tahap 3 — Penyusunan User Flow


## Role

Kamu adalah UX Designer dan Interaction Analyst.


## Task

Buat user flow untuk fitur AI clustering.


## Context

Fitur:

Analisis pola hafalan santri.


Status AI wajib:

1. Validasi data.
2. Proses loading.
3. Analisis algoritma.
4. Hasil clustering.
5. Fallback ketika gagal.


## Output

Buat:

- Alur pengguna.
- Diagram Mermaid.
- Status sistem AI.


---

# 8. Koreksi Manual User Flow


Perubahan yang dilakukan:


Sebelum:

Login → Analisis → Hasil


Sesudah:

Login

↓

Pilih Dataset

↓

Validasi Data

↓

Preprocessing

↓

K-Means

↓

K-Medoids

↓

Evaluasi

↓

Visualisasi

↓

Laporan


Alasan:

Menambahkan proses validasi dan tahapan machine learning.


---

# 9. Prompt Tahap 4 — Penyusunan Acceptance Criteria


## Role

Kamu adalah QA Engineer dan Test Analyst.


## Task

Buat Acceptance Criteria menggunakan format Given-When-Then.


## Context

Fitur:

Analisis clustering pola hafalan.


## Output

Buat skenario:

- Normal flow.
- Data tidak valid.
- Kegagalan proses.


---

# 10. Draft Awal Acceptance Criteria


AI menghasilkan:


Scenario:

Analisis berhasil.


Given:

Dataset tersedia.


When:

Pembina menjalankan clustering.


Then:

Sistem menampilkan hasil cluster.


---

# 11. Koreksi Manual Acceptance Criteria


Penyesuaian:

Tambahkan kondisi pengujian:

1. Dataset kosong.
2. Data tidak lengkap.
3. Service clustering gagal.


Tujuan:

Memastikan fitur AI dapat diuji pada kondisi normal dan error.


---

# 12. Validasi Akhir Dokumen


Dokumen akhir telah memenuhi:


✓ User Story berdasarkan Functional Requirement.

✓ Use Case memiliki alur utama dan alternatif.

✓ User Flow memiliki proses AI.

✓ Acceptance Criteria menggunakan format Given-When-Then.

✓ Traceability Matrix menghubungkan FR, User Story, Use Case, dan Acceptance Criteria.


---

# 13. Catatan Tim


AI digunakan sebagai alat bantu penyusunan dokumen kebutuhan perangkat lunak.

Seluruh hasil generate AI telah melalui proses:

1. Review kebutuhan proyek.
2. Penyesuaian dengan SRS.
3. Validasi aktor pengguna.
4. Koreksi struktur kebutuhan.
5. Pemeriksaan keterlacakan kebutuhan.