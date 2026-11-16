print("====================================")
print("     SISTEM PENILAIAN AKADEMIK")
print("====================================")

# Input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

# Menyiapkan penyimpanan data
data_mahasiswa = []

jumlah_lulus = 0
jumlah_tidak_lulus = 0

# Proses input beberapa mahasiswa
for i in range(jumlah):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Masukkan nama mahasiswa: ")
    nilai = int(input("Masukkan nilai mahasiswa: "))

    # Menentukan kategori nilai
    if nilai >= 85 and nilai <= 100:
        kategori = "A"
        keterangan = "Sangat Baik"
        status = "LULUS"

    elif nilai >= 75:
        kategori = "B"
        keterangan = "Baik"
        status = "LULUS"

    elif nilai >= 60:
        kategori = "C"
        keterangan = "Cukup"
        status = "LULUS"

    elif nilai >= 0:
        kategori = "D"
        keterangan = "Tidak Lulus"
        status = "TIDAK LULUS"

    else:
        print("Nilai tidak valid!")
        continue

    # Menyimpan data mahasiswa
    data_mahasiswa.append(
        [nama, nilai, kategori, keterangan, status]
    )

    # Menghitung jumlah kelulusan
    if status == "LULUS":
        jumlah_lulus += 1
    else:
        jumlah_tidak_lulus += 1


# Menampilkan seluruh hasil
print("\n====================================")
print("       HASIL PENILAIAN MAHASISWA")
print("====================================")

for data in data_mahasiswa:
    print("\nNama       :", data[0])
    print("Nilai      :", data[1])
    print("Kategori   :", data[2])
    print("Keterangan :", data[3])
    print("Status     :", data[4])

# Menampilkan jumlah kelulusan
print("\n====================================")
print("          REKAPITULASI")
print("====================================")
print("Jumlah mahasiswa     :", len(data_mahasiswa))
print("Jumlah mahasiswa lulus:", jumlah_lulus)
print("Jumlah tidak lulus    :", jumlah_tidak_lulus)
print("====================================")
print("       PROGRAM SELESAI")