# Menghitung luas dan volume balok || HAFIDH AHMAD FAUZAN
# NAMA  : HAFIDH AHMAD FAUZAN
# NIM   : 19051397027
# PRODI : D4 MI 2019 A


# JUDUL
print("\n" + 100 * "=")
print("MENGHITUNG LUAS DAN VOLUME BALOK".center(100))
print(100 * "=" + "\n")


data_panjang = (input(r"Panjang Balok  : "))

# CHECK INPUT PANJGANG BALOK <- must be 5 character and contain only decimal without space
while ((all(char.isnumeric() for char in data_panjang) or
        "." in data_panjang) and
       (data_panjang.count(".") <= 1) and
       (float(data_panjang) >= 1)) != True:
    print(r"Input is wrong !! panjang only be filled with a min-value 1 with max 2 decimal (.00) and contains only numeric without space or character" + "\n")
    data_panjang = (input(r"Panjang Balok : "))


data_lebar = (input(r"Lebar Balok    : "))

# CHECK INPUT PANJGANG BALOK <- must be 5 character and contain only decimal without space
while ((all(char.isnumeric() for char in data_lebar) or
        "." in data_lebar) and
       (data_lebar.count(".") <= 1) and
       (float(data_lebar) >= 1)) != True:
    print(r"Input is wrong !! lebar only be filled with a min-value 1 with max 2 decimal (.00) and contains only numeric without space or character" + "\n")
    data_lebar = (input(r"Lebar Balok   : "))


data_tinggi = (input(r"Tinggi Balok   : "))

# CHECK INPUT PANJGANG BALOK <- must be 5 character and contain only decimal without space
while ((all(char.isnumeric() for char in data_tinggi) or
        "." in data_tinggi) and
       (data_tinggi.count(".") <= 1) and
       (float(data_tinggi) >= 1)) != True:
    print(r"Input is wrong !! tinggi only be filled with a min-value 1 with max 2 decimal (.00) and contains only numeric without space or character" + "\n")
    data_tinggi = (input(r"Tinggi Balok   : "))


# CASTING TIPE-DATA STRING TO FLOAT
v_panjang = float(data_panjang)
v_lebar = float(data_lebar)
v_tinggi = float(data_tinggi)

# CHECK TIPE-DATA
# print(type(v_panjang))
# print(type(v_lebar))
# print(type(v_tinggi))

# RUMUS
luas = 2 * ((v_panjang * v_lebar) +
            (v_panjang * v_tinggi) +
            (v_lebar * v_tinggi))

volume = v_panjang * v_lebar * v_tinggi

# OUTPUT
print("\n" + 100 * "=")
print("HASIL LUAS DAN VOLUME BALOK".center(100))
print(100 * "=" + "\n")

print(f"Panjang Balok  : {v_panjang:.2f}")
print(f"Lebar Balok    : {v_lebar:.2f}")
print(f"Tinggi Balok   : {v_tinggi:.2f}")
print(f"Luas Balok     : {luas:.2f}")
print(f"Volume Balok   : {volume:.2f}")

print("\n" + 100 * "=" + "\n")
