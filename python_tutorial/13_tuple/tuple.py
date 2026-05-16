# Tupel digunakan untuk menyimpan beberapa item dalam satu variabel.
# Tupel adalah koleksi yang dipesan dan tidak dapat diubah.

# Tupel ditulis dengan tanda kurung bulat.
thistuple = ("apple", "banana", "cherry")
print(thistuple)


# Item tupel diurutkan, tidak dapat diubah, dan memungkinkan nilai duplikat.
# Ketika kita mengatakan bahwa tupel diurutkan, itu berarti item tersebut 
# memiliki urutan yang ditentukan, dan urutan tersebut tidak akan berubah.
# Tupel tidak dapat diubah, artinya kita tidak dapat mengubah, menambah, 
# atau menghapus item setelah tupel dibuat


# Karena tupel diindeks, mereka dapat memiliki item dengan nilai yang sama
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# Untuk menentukan berapa banyak item yang dimiliki tupel, gunakan len() fungsi:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# Untuk membuat tuple dengan hanya satu item, Anda harus menambahkan koma setelah item,
# jika tidak, Python tidak akan mengenalinya sebagai tupel.
thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple") # bukan tuple
print(type(thistuple))


# Item tuple dapat berupa tipe data apa pun:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# Sebuah tuple dapat berisi tipe data yang berbeda:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)


# Dari perspektif Python, tupel didefinisikan sebagai objek dengan tipe data 'tuple'
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


# Dimungkinkan juga untuk menggunakan tupel() konstruktor untuk membuat tupel.
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)