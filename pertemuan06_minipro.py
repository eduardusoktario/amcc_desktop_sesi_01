angka_satu =  int(input("Masukkan angka pertama >> "))
angka_dua =  int(input("Masukkan angka kedua >> "))

def tambah():
    jumlahin = angka_satu + angka_dua
    return print(jumlahin)

def kurang():
    kurangin = angka_satu - angka_dua
    return print(kurangin)

def kali():
    kaliin = angka_satu * angka_dua
    return print(kaliin)

def bagi():
    bagiin = angka_satu / angka_dua
    return print(bagiin)

def menu():
    print("\n")
    print(">>>>> MENU <<<<<")
    print("[1] Penjumlahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")

    pilih_menu = input("Pilih Menu 1/2/3/4 >> ")

    if pilih_menu == "1" :
        tambah()
    elif pilih_menu == "2" :
        kurang()
    elif pilih_menu == "3" :
        kali()
    elif pilih_menu == "4" :
        bagi()
    else :
        exit()

if __name__ == "__main__" :
    while(True):
        menu()