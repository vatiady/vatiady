# Belajar List

# cara ke 1
""" nama1 = "reza"
nama2 = "raka"
nama3 = "andin"
 """
 #cara ke 2
""" nama = []
nama.append("reza")
nama.append("raka")
nama.append("andin")
print(nama) """

#cara ke 3
nama = ["reza","raka","andin"]
nama.append("gian")

print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3])

#Untuk mengetahui jumlah data di List
print("jumlahnya adalah", len(nama))

#Untuk menghapus indeks
nama.remove("reza")
print(nama)
print("jumlah setelah dihapus adalah", len(nama))
