# Membuat Program For-Loop dan Range

banyak = int(input("berapa banyak datanya? "))

nama = []
umur = []

#Pertama minta minta dulu datanya
for i in range(0,banyak):
    print(f"data ke {i}")
    input_nama = input("Nama : ") #membuat variabel untuk dipanggil pada append
    input_umur = int(input("Umur : ")) #membuat variabel untuk dipanggil pada append

#Kemudian data yang telah diinput dimasukkan ke list
    nama.append(input_nama) #memanggil variabel untuk dimasukkan ke array nama
    umur.append(input_umur) #memanggil variabel untuk dimasukkan ke array umur

#Selanjutnya menampilkan data ke display
for i in range(0,len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur}")