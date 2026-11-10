import modul_sensor

# List kosong untuk menyimpan data bertipe tuple
log_kebun = []


def input_sensor():
    """Meminta input suhu & kelembaban secara aman.
    Mengembalikan tuple (suhu, kelembaban)."""
    while True:
        try:
            suhu = float(input("Masukkan Suhu Udara (C) [0-100]: "))
            lembab = float(input("Masukkan Kelembaban Tanah (%) [0-100]: "))

            if 0 <= suhu <= 100 and 0 <= lembab <= 100:
                return (suhu, lembab)
            else:
                print("Error: Nilai harus di rentang 0-100. Coba lagi.\n")
        except ValueError:
            print("Error: Input harus berupa angka, bukan huruf. Coba lagi.\n")


def rekam_data():
    data = input_sensor()
    log_kebun.append(data)
    print(f"Data {data} berhasil direkam. Total data: {len(log_kebun)}\n")


def analisis_tren():
    if len(log_kebun) == 0:
        print("Belum ada data. Silakan rekam data dulu (menu 1).\n")
        return

    # Slicing: ambil maksimal 3 data terakhir
    tiga_terakhir = log_kebun[-3:]

    print(f"\n=== Analisis Tren {len(tiga_terakhir)} Data Terakhir ===")
    print(f"Lokasi: {modul_sensor.LOKASI[0]} "
          f"({modul_sensor.LOKASI[1]}, {modul_sensor.LOKASI[2]})")

    # Iterasi dengan for
    for i, (suhu, lembab) in enumerate(tiga_terakhir, start=1):
        print(f"Data {i}: Suhu = {suhu} C | Kelembaban = {lembab} %")

    # Panggil fungsi dari modul
    rata_suhu, rata_lembab = modul_sensor.hitung_tren(tiga_terakhir)
    status = modul_sensor.evaluasi_irigasi(
        rata_suhu, rata_lembab, modul_sensor.AMBANG_KRITIS
    )

    print(f"Rata-rata Suhu       : {rata_suhu:.2f} C")
    print(f"Rata-rata Kelembaban : {rata_lembab:.2f} %")
    print(f"Status               : {status}\n")


def main():
    while True:
        print("=== MONITORING IoT KEBUN ===")
        print("[1] Rekam Data")
        print("[2] Analisis Tren (3 Terakhir)")
        print("[3] Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            rekam_data()
        elif pilihan == "2":
            analisis_tren()
        elif pilihan == "3":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Pilih 1, 2, atau 3.\n")


main()