# Belajar Continue
#fungsinya untuk men skip proses yang ada di dalam loop
for i in range(1,100):
    #jika hasil modulusnya = 0 maka continue(skip) berarti tidak diprint
    if i % 2 == 0:  #menggunakan operator_perbandingan
        continue
    print(i)