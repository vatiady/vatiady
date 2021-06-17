# Belajar For Loop

pelanggan = ["reza","raka","andin","gian"]
pelanggan.append("nuna")
pelanggan.append("rick")
pelanggan.append("patrick")

#Mengakses semua nama pelanggan?
#Cara ke -1 Ribet
""" print(pelanggan[0])
print(pelanggan[1])
print(pelanggan[2])
print(pelanggan[3])
 """

 #Cara ke  -2
for nama in pelanggan:
   print("=======================")
   print(f"|nama pelanggan: {nama} |")