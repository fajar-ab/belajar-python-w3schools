# union() method mengembalikan set baru dengan semua item dari kedua set
set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3}

x = set_1.union(set_2)

print(x)

# dapat menggunakan | operator, bukan union() metode, dan akan mendapatkan hasil yang sama
x = set_1 | set_2

print(x)


# Semua metode dan operator penggabungan dapat digunakan untuk menggabungkan beberapa set
set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3, 4}
set_3 = {"John", "Elena"}
set_4 = {"apple", "banana", "cherry"}

myset = set_1.union(set_2, set_3, set_4)
print(myset)

myset = set_1 | set_2 | set_3 | set_4
print(myset)


# join dengan satu set dengan tupel
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# The  | operator hanya memungkinkan untuk bergabung set dengan set, 
# dan tidak dengan tipe data lain seperti dapat dengan  union() method


# update() metode menyisipkan semua item dari satu set ke set lainnya
# mengubah set asli, dan tidak mengembalikan set baru
set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3}

set_1.update(set_2)
print(set_1)

# Keduanya union() and update() akan mengecualikan item duplikat apa pun


# intersection() metode akan mengembalikan himpunan baru, yang hanya berisi item yang ada di kedua himpunan.
set_1 = {"apple", "banana", "cherry"}
set_2 = {"google", "microsoft", "apple"}

set_3 = set_1.intersection(set_2)
print(set_3)

# dapat menggunakan & operator, bukan metode, dan akan mendapatkan hasil yang sama. intersection()
set_3 = set_1 & set_2
print(set_3)

# & operator hanya memungkinkan untuk bergabung set dengan set, dan tidak 
# dengan tipe data lain seperti dapat dengan intersection() method.


# intersection_update() metode juga akan menyimpan HANYA duplikat, 
# tapi itu akan mengubah set asli alih-alih mengembalikan set baru
set_1 = {"apple", "banana", "cherry"}
set_2 = {"google", "microsoft", "apple"}

set_1.intersection_update(set_2)
print(set_1)


# Nilai-nilainya True and 1 dianggap sebagai nilai yang sama. Hal yang sama berlaku untuk False and 0.
set_1 = {"apple", 1,  "banana", 0, "cherry"}
set_2 = {False, "google", 1, "apple", 2, True}

set_3 = set_1.intersection(set_2)
print(set_3)


# metode akan kembalikan set baru yang hanya berisi item dari set pertama
# yang tidak ada di set lainnya.difference()
set_1 = {"apple", "banana", "cherry"}
set_2 = {"google", "microsoft", "apple"}

set_3 = set_1.difference(set_2)
print(set_3)

# dapat menggunakan - operator, bukan metode, dan akan mendapatkan hasil yang sama. difference()
set_3 = set_1 - set_2
print(set_3)

# operator hanya memungkinkan untuk bergabung set dengan set, dan tidak dengan tipe data 
# lain seperti dapat dengan difference() method.


# difference_update() metode akan tetap barang-barang dari set pertama yang tidak ada di set lainnya, 
# tapi itu akan mengubah set asli alih-alih mengembalikan set baru.
set_1 = {"apple", "banana", "cherry"}
set_2 = {"google", "microsoft", "apple"}

set_1.difference_update(set_2)
print(set_1)


# symmetric_difference() metode hanya akan menyimpan elemen-elemen yang TIDAK ada di kedua set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

# dapat menggunakan ^ operator, bukan metode, dan Anda akan mendapatkan hasil yang sama. 
# symmetric_difference()
set3 = set1 ^ set2
print(set3)

# The ^ operator hanya memungkinkan Anda untuk bergabung set dengan set, 
# dan tidak dengan tipe data lain seperti Anda dapat dengan symmetric_difference() method.


# symmetric_difference_update() metode juga akan menjaga semua tetapi duplikatnya, 
# tapi itu akan mengubah set asli alih-alih mengembalikan set baru.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)