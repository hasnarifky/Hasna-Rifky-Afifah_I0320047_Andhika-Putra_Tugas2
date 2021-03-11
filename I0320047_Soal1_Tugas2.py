print("Soal 1")
print("Program perhitungan")
print(" ")

#Menghitung luas persegi panjang
print("1. Luas persegi panjang")
print("Masukkan data yang dibutuhkan")
panjang = float(input("panjang persegi panjang(p): "))
lebar = float(input("lebar persegi panjang(l): "))
luas = panjang * lebar
print("Luas persegi panjang : ", luas)
print(" ")

#Menghitung luas lingkaran
print("2. Luas lingkaran")
print("Masukkan data yang dibutuhkan")
r = float(input("jari-jari lingkaran(r): "))
luas_lingkaran = 3.14 * (r ** 2)
print("Luas lingkaran : ", luas_lingkaran)
print(" ")

#Menghitung luas kubus
print("3. Luas kubus")
print("Masukkan data yang dibutuhkan")
s = float(input("sisi kubus(s): "))
luas_kubus = 6 * (s * s)
print("Luas kubus : ", luas_kubus)
print(" ")

#Menghitung konversi suhu celcius ke fahrenheit
print("4. Konversi suhu celcius ke fahrenheit")
print("Masukkan data yang dibutuhkan")
C = float(input("suhu celcius(C): "))
F = ((9 * C) / 5) + 32
print("Suhu fahrenheit(F) : ", F)
print(" ")

#Menghitung konversi suhu reamur ke kelvin
print("5. Konversi suhu reamur ke kelvin")
print("Masukkan data yang dibutuhkan")
R = float(input("suhu reamur(R): "))
K = ((5 * R) / 4) + 273
print("Suhu kelvin(K) : ", K)
