
def periksa_jawaban(jawaban_pengguna, jawaban_benar):
    return jawaban_pengguna == jawaban_benar


def hitung_nilai(benar, jumlah_soal):
    if jumlah_soal == 0:
        return 0

    nilai = (benar / jumlah_soal) * 100
    return round(nilai, 2)


def evaluasi_latihan(daftar_soal, daftar_jawaban):
    benar = 0

    for i in range(len(daftar_soal)):
        if periksa_jawaban(
            daftar_jawaban[i],
            daftar_soal[i]["jawaban"]
        ):
            benar += 1

    salah = len(daftar_soal) - benar
    nilai = hitung_nilai(benar, len(daftar_soal))

    return benar, salah, nilai


def berikan_feedback(nilai):
    if nilai >= 85:
        return "Sangat baik! Pertahankan prestasimu."
    elif nilai >= 70:
        return "Bagus! Terus tingkatkan kemampuanmu."
    elif nilai >= 50:
        return "Cukup baik, tetap semangat belajar."
    else:
        return "Jangan menyerah, ayo berlatih lagi!"