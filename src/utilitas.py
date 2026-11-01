
def tampilkan_menu():
    print("\n===== MATHQUIZ =====")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")


def pilih_operasi():
    pilihan = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/"
    }

    while True:
        tampilkan_menu()
        pilih = input("Pilih operasi (1-4): ")

        if pilih in pilihan:
            return pilihan[pilih]

        print("Pilihan tidak valid! Silakan coba lagi.")


def input_jumlah_soal():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah soal: "))

            if jumlah > 0:
                return jumlah

            print("Jumlah soal harus lebih dari 0.")

        except ValueError:
            print("Input harus berupa angka bulat!")


def input_nama():
    while True:
        nama = input("Masukkan nama pengguna: ").strip()

        if nama:
            return nama

        print("Nama tidak boleh kosong!")


def input_jawaban():
    while True:
        try:
            return int(input("Jawaban Anda: "))
        except ValueError:
            print("Jawaban harus berupa angka bulat!")