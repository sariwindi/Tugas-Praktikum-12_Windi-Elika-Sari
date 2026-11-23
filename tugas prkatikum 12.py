import math

# a. fungsi luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# b. fungsi volume balok
def volume_persegi_panjang(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# c. fungsi luas lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

# d. fungsi volume bola
def volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari ** 3

# input luas persegi panjang 
print("=== LUAS PERSEGI PANJANG ===")
p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))
print("Luas persegi panjang =", luas_persegi_panjang(p, l,))

# input volume balok
print("=== volume balok ===")
p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))
t = float(input("Masukkan tinggi: "))
print("Volume balok =", volume_persegi_panjang(p, l, t))

# input luas lingkaran
print("=== LUAS LINGKARAN ===")
r = float(input("Masukkan jari-jari: "))
print("Luas lingkaran =", luas_lingkaran(r))

# input volume bola
print("\n=== VOLUME BOLA ===")
r = float(input("Masukkan jari-jari: "))
print("Volume bola =",volume_bola(r))

