print("Soal 2")
print("Program yang mencakup tipe data string, integer, dan float")
print(" ")

#Variabel biodata
nama_lengkap = "Hasna Rifky Afifah"
nama_panggilan = "Hasna"
alamat_rumah = "Palur, Mojolaban, Sukoharjo"
jurusan_kuliah = "Teknik Industri"
universitas = "UNS"
angkatan = 2020
hobi = "mendengarkan lagu dan membaca"
tinggi_badan = 173
ukuran_sepatu = tinggi_badan - 133

#Variabel menghitung usia
bulan_lahir = 5
tahun_lahir = 2002
tanggal_sekarang = 11
bulan_sekarang = 3
tahun_sekarang = 2021
umur_dalam_bulan = (tahun_sekarang - tahun_lahir) * 12 + (bulan_sekarang - bulan_lahir)
umur_dalam_tahun = float(umur_dalam_bulan / 12)
umur_dalam_hari = int(umur_dalam_tahun * 365) + 5
tahun = int(umur_dalam_hari / 365)
bulan = int((umur_dalam_hari - (tahun * 365)) / 30)
selisih_hari = (228 - umur_dalam_bulan) * 30 + (31 - tanggal_sekarang) + 1

print("Deskripsi diri")
print(" ")
print("Nama saya", nama_lengkap)
print("Biasa dipanggil", nama_panggilan)
print("Saat ini, saya berkuliah di", jurusan_kuliah, universitas, "angkatan tahun", angkatan)
print("Saya tinggal di", alamat_rumah)
print("Saya senang", hobi, "di waktu luang")
print("Tinggi badan saya yaitu", tinggi_badan, "cm")
print("Ukuran sepatu saya yaitu", ukuran_sepatu)
print("Saat ini, saya berusia", umur_dalam_tahun, "tahun")
print("Tepatnya", tahun, "tahun", bulan, "bulan")
print("Saya akan genap berusia", tahun_sekarang - tahun_lahir, "tahun", selisih_hari, "hari lagi")
