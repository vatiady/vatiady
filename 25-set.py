#Belajar Set

#list => []
# tuple => ()
# set => {}

#perbedaan ketiganya yaitu list & tuple dapat menerima data duplikat
#sedangkan set tidak ada duplikasi data (unique)
#-dalam set tidak mendukung pengambilan data menggunakan indeks karena urutannya berubah ubah ketika di print
#-tidak ada mengubah data menggunakan indeks

#cara memanggil data menggunakan fungsi For-Loop

#hanya bisa menambah data dan menghapus data
nama = {"Reza","Raka","Andin"}

nama.add("Gian")

for data in nama:
    print(data)

nama.remove("Reza")

print(nama)
