def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka, total)

list_angka, total = jumlahkan(3,5,6,7,34,56)

print(f"Total {list_angka} = {total}")