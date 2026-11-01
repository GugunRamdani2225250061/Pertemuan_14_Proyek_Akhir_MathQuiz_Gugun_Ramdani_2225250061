def simpan_riwayat(nama, jumlah_soal, benar, salah, nilai):
    with open("data/riwayat_latihan.txt", "a") as file:
        file.write("\n=== HASIL LATIHAN ===\n")
        file.write(f"Nama: {nama}\n")
        file.write(f"Jumlah Soal: {jumlah_soal}\n")
        file.write(f"Jawaban Benar: {benar}\n")
        file.write(f"Jawaban Salah: {salah}\n")
        file.write(f"Nilai: {nilai}\n")