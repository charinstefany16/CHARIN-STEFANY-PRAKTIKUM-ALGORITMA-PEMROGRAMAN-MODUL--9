def write():
   
    nama = input("Masukkan Nama mu: ")
    umur = input("Masukkan Umur mu: ")
    alamat = input("Masukkan Alamatmu: ")
    email = input("Masukkan Emailmu: ")
    dosen = input("Masukkan Dosen Walimu: ")

    
    with open("Biodata.txt", "w") as filenulis:
        filenulis.write(f"Nama: {nama}\n")
        filenulis.write(f"Umur: {umur}\n")
        filenulis.write(f"Alamat: {alamat}\n")
        filenulis.write(f"Email: {email}\n")
        filenulis.write(f"Dosen: {dosen}\n")

def read():
    
    with open("Biodata.txt", "r") as filebaca:
        text = filebaca.read()
        print("Berikut Ini Data Kamu:")
        print(text)

write()
print("\n")  
read()