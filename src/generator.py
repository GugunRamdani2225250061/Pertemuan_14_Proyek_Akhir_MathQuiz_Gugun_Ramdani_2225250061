
import random

def buat_soal(operasi):
    angka1 = random.randint(1, 20)
    angka2 = random.randint(1, 20)

    if operasi == "+":
        jawaban = angka1 + angka2
    elif operasi == "-":
        jawaban = angka1 - angka2
    elif operasi == "*":
        jawaban = angka1 * angka2
    elif operasi == "/":
        angka2 = random.randint(1, 10)
        jawaban = angka1
        angka1 = angka1 * angka2
    else:
        return None

    soal = f"{angka1} {operasi} {angka2}"
    return {
        "soal": soal,
        "jawaban": jawaban
    }


def buat_daftar_soal(jumlah, operasi):
    daftar_soal = []

    for i in range(jumlah):
        soal = buat_soal(operasi)
        daftar_soal.append(soal)

    return daftar_soal