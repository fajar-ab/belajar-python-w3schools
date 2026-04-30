"""
tidak dapat menyalin list hanya dengan mengetik

list2 = list1

karna `list2` hanya akan menjadi sebuah referensi ke `list1`, dan perubahan yang
di lakukan i `list1` otomatis juga akan dibuat di `list2`
"""

# dapat menggunakan method list bawaan copy() untuk menyalin list
this_list = ["apple", "banana", "cherry"]
my_list = this_list.copy()

print(this_list)

# cara lain untuk membuat salinan adalah dengan menggunakan method bawaan list()
this_list = ["apple", "banana", "cherry"]
my_list = list(this_list)

print(this_list)

# juga dapat membuat salinan list dengan mengunakan : (irisan) operator
this_list = ["apple", "banana", "cherry"]
my_list = this_list[:]

print(my_list)