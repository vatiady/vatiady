#Belajar Argument List (*)
#cara rumit
""" def jumlahkan(satu, dua):
    total= satu + dua
    print(f"{satu} + {dua} = {total}")

jumlahkan(4,5) """

#cara argument list
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")

jumlahkan(1,3,63,2,5)