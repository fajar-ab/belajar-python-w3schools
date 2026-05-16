# Tupel tidak dapat diubah, artinya Anda tidak dapat mengubah, 
# menambah, atau menghapus item setelah tupel dibuat.

# Ubah tuple menjadi list untuk dapat mengubahnya
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Karena tupel tidak dapat diubah, tupel tidak memiliki built-in 
# append() metode, tetapi ada cara lain untuk menambahkan item ke tupel.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)


# Tambahkan tupel ke tupel. diperbolehkan untuk menambahkan tupel ke tupel, 
# jadi jika ingin menambahkan satu item, (atau banyak), buat tupel baru dengan item(s),
# dan menambahkannya ke tuple yang ada:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# Tupel adalah tidak dapat diubah, sehingga tidak dapat menghapus item dari itu, 
# tetapi dapat menggunakan solusi yang sama seperti yang kami gunakan 
# untuk mengubah dan menambahkan item tupel:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

# Atau dapat menghapus tupel sepenuhnya:
thistuple = ("apple", "banana", "cherry")
del thistuple

print(thistuple) # Ini akan menimbulkan kesalahan karena tuple tersebut sudah tidak ada lagi.

