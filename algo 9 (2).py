import os

def buat_dan_tulis_file():
    nama_file = input("Masukkan Nama File: ")
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    tahun = input("Masukkan tahun angkatanmu: ")

    with open(nama_file, 'w') as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"NIM: {nim}\n")
        file.write(f"Angkatan: {tahun}\n")

    print("\nFile Berhasil Dibuat\n")

def baca_file():
    nama_file = input("Masukkan Nama File: ")
    if os.path.exists(nama_file):
        with open(nama_file, 'r') as file:
            print("\nIsi File:")
            print(file.read())
    else:
        print("\nFile tidak ditemukan!\n")

def tambah_text_ke_file():
    nama_file = input("Masukkan Nama File: ")
    if os.path.exists(nama_file):
        tambahan = input("Masukkan text tambahan: ")
        with open(nama_file, 'a') as file:
            file.write(f"{tambahan}\n")
        print("\nText berhasil ditambahkan\n")
    else:
        print("\nFile tidak ditemukan!\n")

def menu():
    while True:
        print(" Program File Handling ")
        print("1. Membuat dan Menulis File")
        print("2. Membaca File")
        print("3. Menambahkan Text Pada File")
        print("4. Keluar Dari Program")

        pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")

        if pilihan == '1':
            buat_dan_tulis_file()
        elif pilihan == '2':
            baca_file()
        elif pilihan == '3':
            tambah_text_ke_file()
        elif pilihan == '4':
            print("\nTerima kasih telah menggunakan program ini!\n")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi!\n")

if __name__ == "__main__":
    menu()