# Setelah satu set dibuat, tidak dapat mengubah itemnya, te
# tapi dapat menambahkan item baru.

# Tambahkan item ke satu set, menggunakan add() method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)

# Untuk menambahkan item dari set lain ke dalam set saat ini, gunakan update() method
fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "manggo", "papaya"}

fruits.update(tropical)
print(fruits)

# Objek di update() metode tidak memiliki untuk menjadi satu set, itu bisa berupa 
# objek apa pun yang dapat diulang (tupel, daftar, kamus dll.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)
