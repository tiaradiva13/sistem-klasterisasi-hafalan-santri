from pydantic import BaseModel
from datetime import date
from typing import Optional


class Santri(BaseModel):
    id_santri: int
    nis: str
    nama: str
    kelas: str
    jenis_kelamin: str
    tanggal_lahir: Optional[date] = None
    alamat: Optional[str] = None


class Hafalan(BaseModel):
    id_hafalan: int
    id_santri: int
    juz: int
    surat: str
    ayat_mulai: int
    ayat_selesai: int
    jumlah_ayat: int
    tanggal_setoran: date
    nilai_hafalan: float
    kualitas_bacaan: float


class Evaluasi(BaseModel):
    id_evaluasi: int
    id_hafalan: int
    kelancaran: float
    tajwid: float
    makhraj: float
    catatan: Optional[str] = None
    tanggal_eval: date


class HasilCluster(BaseModel):
    id_cluster: int
    id_santri: int
    cluster_id: int
    nama_cluster: str
    nilai_akhir: float
    tanggal_proses: date


class SantriCreate(BaseModel):
    nis: str
    nama: str
    kelas: str
    jenis_kelamin: str
    tanggal_lahir: Optional[date] = None
    alamat: Optional[str] = None


class HafalanCreate(BaseModel):
    id_santri: int
    juz: int
    surat: str
    ayat_mulai: int
    ayat_selesai: int
    jumlah_ayat: int
    tanggal_setoran: date
    nilai_hafalan: float
    kualitas_bacaan: float


class EvaluasiCreate(BaseModel):
    id_hafalan: int
    kelancaran: float
    tajwid: float
    makhraj: float
    catatan: Optional[str] = None
    tanggal_eval: date


class ClusterRequest(BaseModel):
    jumlah_cluster: int


class ClusterResponse(BaseModel):
    id_santri: int
    cluster_id: int
    nama_cluster: str
    nilai_akhir: float
    tanggal_proses: date