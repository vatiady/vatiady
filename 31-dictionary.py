#Belajar Tipe Data Dictionary

#data pertama key-value
customer = {"Name":"Reza","Age":"25","Address":"Kuripan"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

#hanya key nya saja yang ditampilkan
""" for data in customer:
    print(data) """

#perulangan meggunakan key-value
""" for key in customer:
    value = customer[key]
    print(f"{key}:{value}")
 """
#perulangan menggunakan tuple
 #pada ditionary memiliki method yang bernama items(data dictionary berupa tuple)
""" print(customer.items()) """ # hanya contoh method items berupa tuple (bukan bagian dari code)
#cara pertama
""" for key in customer.items():
    print(f"{key[0]}:{key[1]}")
 """
 #menambahkan/mengubah data baru di dalam dictionary
customer["Company"] = "X"
customer["Name"] = "Rezalian Vatiady"

#menghapus data
del customer["Company"]

#cara kedua (menggunakan for dua data)
for key, value in customer.items():
    print(f"{key}:{value}")

#note : untuk data yang banyak seperti customer, gunakanlah dictionary
 #karena lebih mudah memanggil nama ditcionary dibandingkan menggunakan indeks pada data yang banyak
 