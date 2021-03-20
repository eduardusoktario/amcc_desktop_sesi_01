# pilihan = input("Lanjut? (yes / no) = ")

# if pilihan.casefold() == "yes" :
#     print("A")
# elif pilihan.casefold() == "no" :
#     print("B")
# else :
#     print("Hai.")

# #yes --> upper() --> YES

# def sapaan(nama) :
#     print("Hello, " +nama)

# sapaan("Yaumil")
# sapaan("Fauzi")
# sapaan("Rio")
# sapaan()

# #Non-Void Function
# def fungsi_satu():
#     print("Hello World")
#     #gaada nilai balik
# #Void Function
# def fungsi_dua():
#     return print("Hello World")
#     #ada nilai balik, yaitu Hello World

# fungsi_satu()
# fungsi_dua()

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     #luas = 10 * 6
#     return luas
#     #return luas = 60
# #luas_persegi_panjang = '60'

# def volume_balok(panjang, lebar, tinggi):
#     volume = luas_persegi_panjang(panjang, lebar) * tinggi
#     # volume = 60 * 8
#     print(volume) 
#     #volume = 480
# #hasil = 480

# volume_balok(10, 6, 8)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def volume_kubus(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print(volume)

# volume_persegi(10)

#Global Variabel
laptop = "Macbook Air M1"
harga = "Rp 20.000.000"

def cek_laptop():
    #Local Variabel
    laptop = "ASUS TUF FX505"
    harga = "Rp 10.500.000"
    print(laptop, harga)

cek_laptop()

print("Hello World")
# Pembacaan = Lokal - Global - Built-in