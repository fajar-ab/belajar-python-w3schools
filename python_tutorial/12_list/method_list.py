# Menambahkan elemen di akhir daftar
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits.append("orange") # method ini menambahkan elemen ke akhir daftar
print(fruits)


# Menghapus semua elemen dari daftar
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits)

fruits.clear() # method ini menghapus semua elemen dari sebuah daftar
print(fruits)


# Mengembalikan salinan daftar tersebu
fruits = ["apple", "banana", "cherry"]
print(fruits)

x = fruits.copy() # Method ini mengembalikan salinan dari daftar yang ditentukan
print(x)


# Mengembalikan jumlah elemen dengan nilai yang ditentukan
fruits = ["apple", "banana", "cherry"]

x = fruits.count("banana") # Method ini mengembalikan jumlah elemen dengan nilai yang ditentukan
print(x)


# Tambahkan elemen-elemen dari sebuah daftar (atau objek iterable lainnya) ke akhir daftar saat ini
fruits = ["apple", "banana", "cherry"]
cars = ["Ford", "BMW", "Volvo"]

# Method ini menambahkan elemen daftar yang ditentukan (atau iterable apa pun) ke akhir daftar saat ini
fruits.extend(cars)
print(fruits)


# Mengembalikan indeks elemen pertama dengan nilai yang ditentukan
fruits = ["apple", "banana", "cherry"]

x = fruits.index("banana") # Method ini hanya mengembalikan kemunculan pertama dari nilai tersebut
print(x)


# Menambahkan elemen pada posisi yang ditentukan
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits.insert(1, "orange") # Metode ini menyisipkan nilai yang ditentukan pada posisi yang ditentukan
print(fruits)


# Menghapus elemen pada posisi yang ditentukan
fruits = ["apple", "banana", "cherry"]

# Angka yang menentukan posisi elemen yang ingin Anda hapus, nilai defaultnya adalah 1, 
# yang akan mengembalikan item terakhir.
x = fruits.pop(1)
print(fruits)
print(x, "dihapus dari list")


# Menghapus item dengan nilai yang ditentukan
fruits = ['apple', 'banana', 'cherry']
print(fruits)

fruits.remove("banana") # Method ini menghapus kemunculan pertama elemen dengan nilai yang ditentukan
print(fruits)


# Membalikkan urutan daftar
fruits = ['apple', 'banana', 'cherry']
print(fruits, "sebelum")

fruits.reverse() # Method ini membalik urutan pengurutan elemen
print(fruits, "setelah")


# Mengurutkan daftar
cars = ['Ford', 'BMW', 'Volvo']
print(cars, "sebelum")

cars.sort()
print(cars, "setelah")