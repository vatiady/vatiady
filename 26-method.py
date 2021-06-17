#Belajar Membuat Method Function

""" nama = []

nama.append("Reza")
print("==============")
for data in nama:
    print(data)

nama.append("Gian")
print("==============")
for data in nama:
    print(data) """

#cara ke -2
""" nama = []
def print_nama():
    for data in nama:
        print("==============")
        print(data)

nama.append("Reza")
nama.append("Raka")
nama.append("Andin")
print_nama() """

#cara ke- 3
nama = []
def print_nama():
    print("==============")
    for data in nama:
        print(data)

nama.append("Reza")
print_nama()
nama.append("Raka")
print_nama()
nama.append("Andin")
print_nama()