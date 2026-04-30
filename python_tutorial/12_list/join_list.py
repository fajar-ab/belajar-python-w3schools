# ada beberapa cara untuk bergabung atau menggabungkan, dua atau lebih list
# di pyhton. cara yang mudah adalah dengan menggunakan + operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# cara lain untuk menggabungkan dua list adalah dengan menambahkan semua
# item dari list2 ke list1, satu persatu

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# juga dapat menggunakan extend() method, dimana tujuannya adalah untuk menambahkan
# element dari satu list ke list lainya
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)