# Konversi nilai mahasiswa || HAFIDH AHMAD FAUZAN
# NAMA  : HAFIDH AHMAD FAUZAN
# NIM   : 19051397027
# PRODI : D4 MI 2019 A


# JUDUL
print("\n" + 100 * "=")
print("KONVERSI NILAI MAHASISWA".center(100))
print(100 * "=" + "\n")


data_nama = input(r"Nama Lengkap      : ")

# CHECK INPUT NAMA-LENGKAP <- must be at least 3 characters & contain only alphabetic, space, apostrophe ('), and backtick(`)
while ((all(char.isalpha() for char in data_nama) or
        all(char.isspace() for char in data_nama) or
        all(char.isalpha() or char.isspace() for char in data_nama) or
        "'" in data_nama or
        "`" in data_nama) and
       (len(data_nama) >= 3)) != True:
    print(r"Input is wrong !! nama lengkap must be at least 3 characters and contains only alphabetic, space, apostrophe ('), and backtick(`)" + "\n")
    data_nama = input(r"Nama Lengkap      : ")


data_matkul = input(r"Mata Kuliah       : ")

# CHECK INPUT MATAKULIAH <- must be at least 3 character & contain only alpha-numeric and space without character
while ((all(char.isalnum() for char in data_matkul) or
        all(char.isspace() for char in data_matkul) or
        all(char.isalnum() or char.isspace() for char in data_matkul)) and
       (len(data_matkul) >= 3)) != True:
    print(r"Input is wrong !! matakuliah must be at least 3 characters and contains only alpha-numeric and space without character" + "\n")
    data_matkul = input(r"Mata Kuliah       : ")


data_nis = input(r"NIS               : ")

# CHECK INPUT NIS <- must be 11 character and contain only numeric without space or character
while ((all(char.isnumeric() for char in data_nis)) and
       (len(data_nis) == 11)) != True:
    print(r"Input is wrong !! nis must be 11 character and contains only numeric without space or character" + "\n")
    data_nis = input(r"NIS               : ")


data_partisipasi = (input(r"Nilai Partisipasi : "))

# CHECK INPUT PARTISIPASI <- must be 5 character and contain only decimal without space
while ((all(char.isnumeric() for char in data_partisipasi) or
        "." in data_partisipasi) and
       (data_partisipasi.count(".") <= 1) and
       (len(data_partisipasi) <= 5) and
       ((float(data_partisipasi) >= 0) and
        (float(data_partisipasi) <= 100))) != True:
    print(r"Input is wrong !! nilai only be filled with a value range of 0-100 with max 2 decimal (.00) and contains only numeric without space or character" + "\n")
    data_partisipasi = (input(r"Nilai Partisipasi : "))


data_tugas = (input(r"Nilai Tugas       : "))

# CHECK INPUT TUGAS <- must be 5 character and contain only decimal without space
while ((all(char.isnumeric() for char in data_tugas) or
        "." in data_tugas) and
       (data_tugas.count(".") <= 1) and
       (len(data_tugas) <= 5) and
       ((float(data_tugas) >= 0) and
        (float(data_tugas) <= 100))) != True:
    print(r"Input is wrong !! nilai only be filled with a value range of 0-100 with max 2 decimal (.00) and contains only numeric without space or character" + "\n")
    data_tugas = (input(r"Nilai Tugas       : "))


data_uts = (input(r"Nilai UTS         : "))

# CHECK INPUT UTS <- must be 5 character and contain only decimal without space
while ((all(char.isnumeric() for char in data_uts) or
        "." in data_uts) and
       (data_uts.count(".") <= 1) and
       (len(data_uts) <= 5) and
       ((float(data_uts) >= 0) and
        (float(data_uts) <= 100))) != True:
    print(r"Input is wrong !! nilai only be filled with a value range of 0-100 with max 2 decimal (.00) and contains only numeric without space or character" + "\n")
    data_uts = (input(r"Nilai UTS         : "))


data_uas = (input(r"Nilai UAS         : "))

# CHECK INPUT UAS <- must be 5 character and contain only decimal without space
while ((all(char.isnumeric() for char in data_uas) or
        "." in data_uas) and
       (data_uas.count(".") <= 1) and
       (len(data_uas) <= 5) and
       ((float(data_uas) >= 0) and
        (float(data_uas) <= 100))) != True:
    print(r"Input is wrong !! nilai only be filled with a value range of 0-100 with max 2 decimal (.00) and contains only numeric without space or character" + "\n")
    data_uas = (input(r"Nilai UAS         : "))


# CASTING TIPE-DATA STRING TO FLOAT
v_partisipasi = float(data_partisipasi)
v_tugas = float(data_tugas)
v_uts = float(data_uts)
v_uas = float(data_uas)

# CHECK TIPE-DATA
# print(type(data_nama))
# print(type(data_matkul))
# print(type(data_nis))
# print(type(v_partisipasi))
# print(type(v_tugas))
# print(type(v_uts))
# print(type(v_uas))

# RUMUS
v_partisipasi = v_partisipasi * 0.2
v_tugas = v_tugas * 0.3
v_uts = v_uts * 0.2
v_uas = v_uas * 0.3

# TOTAL NILAI
total = v_partisipasi + v_tugas + v_uts + v_uas

# NILAI DAN INDEKS
if total < 40:
    nilai = 0
    indeks = "E"
elif total < 55:
    nilai = 1
    indeks = "D"
elif total < 60:
    nilai = 2
    indeks = "C"
elif total < 65:
    nilai = 2.5
    indeks = "C+"
elif total < 70:
    nilai = 2.75
    indeks = "B-"
elif total < 75:
    nilai = 3
    indeks = "B"
elif total < 80:
    nilai = 3.5
    indeks = "B+"
elif total < 85:
    nilai = 3.75
    indeks = "A-"
elif total <= 100:
    nilai = 4
    indeks = "A"

# OUTPUT
print("\n" + 100 * "=")
print("HASIL KONVERSI NILAI".center(100))
print(100 * "=" + "\n")

print(f"Nama Lengkap      : {data_nama}")
print(f"Mata Kuliah       : {data_matkul}")
print(f"NIS               : {data_nis}")
print(f"Nilai Partisipasi : {v_partisipasi:.2f}")
print(f"Nilai Tugas       : {v_tugas:.2f}")
print(f"Nilai UTS         : {v_uts:.2f}")
print(f"Nilai UAS         : {v_uas:.2f}")
print(f"Nilai Akhir       : {total:.2f}")
print(f"Indeks Angka      : {nilai:d}")
print(f"Indeks Huruf      : {indeks}")

print("\n" + 100 * "=" + "\n")
