# PROPOSAL PROYEK MATHQUIZ

## 1. Judul Proyek
MathQuiz: Program Generator dan Evaluasi Latihan Soal Matematika Berbasis Python.

## 2. Latar Belakang
Matematika membutuhkan latihan secara berulang agar peserta didik dapat memahami konsep dan meningkatkan kemampuan menyelesaikan soal. Pembuatan soal dan pemeriksaan jawaban secara manual membutuhkan waktu. Oleh karena itu, MathQuiz dirancang untuk menghasilkan soal secara acak, memeriksa jawaban, dan menghitung nilai secara otomatis.

## 3. Pengguna dan Tujuan
**Pengguna:**
- Siswa SMP/SMA.
- Guru matematika.
- Peserta didik yang ingin berlatih mandiri.

**Tujuan:**
1. Membantu latihan matematika secara mandiri.
2. Menghasilkan soal secara otomatis.
3. Memeriksa jawaban pengguna.
4. Menghitung nilai akhir.
5. Memberikan evaluasi hasil latihan.

## 4. Ruang Lingkup
**Fitur wajib:**
1. Menampilkan menu operasi matematika.
2. Menghasilkan soal secara acak.
3. Menerima jawaban pengguna.
4. Memeriksa jawaban benar atau salah.
5. Menghitung dan menampilkan nilai akhir.

**Fitur tambahan:**
- Menyimpan riwayat latihan ke file TXT.
- Menampilkan evaluasi hasil belajar.

**Batasan:**
- Menggunakan bahasa Python.
- Berjalan melalui terminal/console.
- Materi meliputi penjumlahan, pengurangan, perkalian, dan pembagian.
- Tidak menggunakan database atau antarmuka grafis.

## 5. Analisis Kebutuhan

### A. Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Menampilkan menu operasi matematika | Wajib |
| F02 | Menghasilkan soal secara acak | Wajib |
| F03 | Menerima jawaban pengguna | Wajib |
| F04 | Memeriksa jawaban | Wajib |
| F05 | Menghitung nilai akhir | Wajib |
| F06 | Menyimpan hasil latihan | Tambahan |

### B. Kebutuhan Nonfungsional
1. Program mudah dijalankan melalui VS Code.
2. Tampilan sederhana dan mudah dipahami.
3. Memiliki pesan kesalahan yang jelas.
4. Mampu menangani input tidak valid.
5. Hasil perhitungan akurat.

## 6. Input, Proses, dan Output (IPO)

| Input | Proses | Output |
|---|---|---|
| Pilihan operasi | Validasi pilihan | Jenis soal |
| Jumlah soal | Menentukan jumlah soal | Soal sesuai jumlah |
| Bilangan acak | Membuat soal matematika | Pertanyaan |
| Jawaban pengguna | Memeriksa jawaban | Benar atau salah |
| Jumlah jawaban benar | Menghitung nilai | Nilai akhir |
| Hasil latihan | Menulis ke file | Riwayat latihan |

## 7. Algoritma dan Pseudocode

**Algoritma:**
1. Mulai program.
2. Tampilkan menu operasi matematika.
3. Pengguna memilih operasi.
4. Validasi pilihan.
5. Masukkan jumlah soal.
6. Program membuat soal secara acak.
7. Pengguna memasukkan jawaban.
8. Program memeriksa jawaban.
9. Hitung jumlah benar dan salah.
10. Hitung nilai akhir.
11. Tampilkan hasil evaluasi.
12. Simpan hasil latihan.
13. Selesai.

**Pseudocode:**

```text
MULAI

Tampilkan menu operasi matematika
Masukkan pilihan pengguna

JIKA pilihan tidak valid:
    Tampilkan pesan kesalahan

Masukkan jumlah soal
Inisialisasi skor = 0

ULANGI sebanyak jumlah soal:
    Buat soal secara acak
    Tampilkan soal
    Masukkan jawaban pengguna

    JIKA jawaban benar:
        Tambahkan skor
        Tampilkan "Jawaban Benar"
    JIKA TIDAK:
        Tampilkan "Jawaban Salah"

Hitung nilai akhir
Tampilkan hasil latihan
Simpan hasil ke file

SELESAI
```

## 8. Struktur Program dan Modularisasi

| Fungsi/Modul | Tanggung Jawab |
|---|---|
| tampilkan_menu() | Menampilkan menu |
| buat_soal() | Menghasilkan soal acak |
| input_pilihan() | Memvalidasi pilihan |
| periksa_jawaban() | Memeriksa jawaban |
| hitung_nilai() | Menghitung nilai akhir |
| simpan_hasil() | Menyimpan hasil latihan |
| main() | Mengatur alur program |

**Struktur Folder:**

```text
Proyek_AkhirMathQuiz
│
├── README.md
├── proposal.md
├── .gitignore
│
├── data/
│   └── riwayat_latihan.txt
│
├── src/
│   ├── main.py
│   ├── generator.py
│   ├── evaluasi.py
│   └── utilitas.py
│
├── tests/
│   └── test_case.md
│
└── output/
    └── .gitkeep
```

## 9. Struktur Data

| Struktur Data | Penggunaan |
|---|---|
| List | Menyimpan kumpulan soal |
| Dictionary | Menyimpan informasi soal dan hasil |
| Integer | Menyimpan bilangan dan skor |
| String | Menyimpan teks soal dan laporan |
| File TXT | Menyimpan riwayat latihan |

Contoh dictionary:

```python
hasil_latihan = {
    "total_soal": 10,
    "benar": 8,
    "salah": 2,
    "nilai": 80
}
```

## 10. Test Case

| ID | Kategori | Input/Kondisi | Expected Result |
|---|---|---|---|
| TC01 | Normal | Memilih penjumlahan | Soal ditampilkan |
| TC02 | Normal | Jawaban benar | Status benar |
| TC03 | Normal | Jawaban salah | Status salah |
| TC04 | Batas | Jumlah soal 1 | Satu soal dibuat |
| TC05 | Invalid | Memilih menu 5 | Pesan kesalahan |
| TC06 | Invalid | Jawaban berupa huruf | Meminta input ulang |
| TC07 | Batas | Semua jawaban benar | Nilai 100 |
| TC08 | Normal | Menyimpan hasil | File berhasil dibuat |

## 11. Pembagian Tugas

| No. | Peran | Tanggung Jawab |
|---|---|---|
| 1 | Koordinator | Mengatur dan mengintegrasikan proyek |
| 2 | Programmer 1 | Membuat generator soal |
| 3 | Programmer 2 | Membuat evaluasi jawaban |
| 4 | Programmer 3 | Membuat program utama |
| 5 | Tester dan Dokumentasi | Pengujian dan dokumentasi |

## 12. Jadwal Pelaksanaan

| Tahapan | Waktu | Target |
|---|---|---|
| Perancangan | Pertemuan 14 | Proposal dan rancangan |
| Implementasi awal | Antara P14–P15 | Pembuatan fitur |
| Integrasi | Pertemuan 15 | Penggabungan program |
| Testing dan debugging | Pertemuan 15 | Pengujian program |
| Dokumentasi | Pertemuan 15 | README dan laporan |
| Presentasi | Pertemuan 16 | Demonstrasi program |

## 13. Repository GitHub

Nama repository: `MathQuiz-Python`

Deskripsi: Program generator dan evaluasi latihan soal matematika berbasis Python.

URL Repository: [Isi URL GitHub kelompok]