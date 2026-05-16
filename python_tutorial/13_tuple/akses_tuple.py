# mengakses item tupel dengan mengacu pada nomor indeks, di dalam kotak bracket:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Item pertama memiliki indeks 0.

# Pengindeksan negatif berarti mulai dari akhir.
# -1 mengacu pada item terakhir, -2 mengacu pada item kedua terakhir dll.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# menentukan rentang indeks dengan menentukan di mana untuk memulai dan di mana untuk akhiri jangkauan.
# Saat menentukan rentang, nilai kembalian akan menjadi tupel baru dengan item yang ditentukan.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# Pencarian akan dimulai pada indeks 2 (termasuk) dan berakhir pada indeks 5 (tidak termasuk).


# Contoh ini mengembalikan item dari awal ke, tetapi TIDAK termasuk, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


# Dengan meninggalkan nilai akhir, rentang akan berlanjut ke akhir tupel:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


# Contoh ini mengembalikan item dari indeks -4 (termasuk) ke indeks -1 (tidak termasuk)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


# Untuk menentukan apakah item tertentu ada dalam tupel, gunakan in keyword:
fruits = ("apple", "banana", "cherry")
if "apple" in fruits:
    print("yes, 'apple' is in the fruits tuple")



