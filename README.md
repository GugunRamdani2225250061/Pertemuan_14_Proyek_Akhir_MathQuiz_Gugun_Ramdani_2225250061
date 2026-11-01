# PERTEMUAN 14 PROYEK AKHIR

- NAMA: GUGUN RAMDANI
- KELAS: 3A
- NIM: 2225250061
- MATA KULIAH: ALGORITMA DAN PEMROGRAMAN

# MathQuiz – Program Latihan Soal Matematika

## Deskripsi
MathQuiz adalah program sederhana berbasis Python yang digunakan untuk membuat dan mengerjakan latihan soal matematika secara acak. Program ini menyediakan operasi penjumlahan, pengurangan, perkalian, dan pembagian serta memberikan nilai berdasarkan jawaban pengguna.

## Fitur
- Membuat soal matematika secara acak.
- Memilih operasi matematika.
- Memeriksa jawaban pengguna.
- Menghitung nilai akhir.
- Memberikan feedback hasil latihan.
- Menyimpan riwayat latihan ke file TXT.

## Teknologi
- Python 3
- Visual Studio Code
- Git dan GitHub

## Struktur Folder
```text
Pertemuan 14_Proyek_Akhir_Gugun Ramdani_2225250061
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
## Cara Menjalankan Program
1. Pastikan Python 3 sudah terinstal.
2. Buka folder MathQuiz di Visual Studio Code.
3. Buka terminal.
4. Jalankan perintah berikut:
```bash
python main.py
```
## Cara Menggunakan
1. Masukkan nama pengguna.
2. Pilih operasi matematika.
3. Masukkan jumlah soal.
4. Jawab soal yang ditampilkan.
5. Lihat hasil dan nilai akhir.
6. Periksa riwayat latihan pada folder `data`.

## Pengujian
Pengujian program dilakukan menggunakan beberapa test case yang mencakup:
- Pengujian operasi matematika.
- Pengujian input pengguna.
- Pengujian pemeriksaan jawaban.
- Pengujian perhitungan nilai.
- Pengujian penyimpanan riwayat.

Dokumentasi pengujian terdapat pada `tests/test_case.md`.

## Penyimpanan Riwayat
Hasil latihan pengguna disimpan secara otomatis dalam file:

`data/riwayat_latihan.txt`

## Tujuan Proyek
Membantu pengguna berlatih dan meningkatkan kemampuan berhitung melalui soal matematika yang sederhana, interaktif, dan mudah digunakan.

## Pengembang
Proyek ini dibuat sebagai tugas mata kuliah Algoritma dan Pemrograman, Program Studi Pendidikan Matematika.
