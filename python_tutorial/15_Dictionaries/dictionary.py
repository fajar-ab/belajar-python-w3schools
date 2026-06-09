# Dictionary

# digunakan untuk menyimpan nilai data dalam pasangan key:value.
# kumpulan yang diurutkan*, dapat diubah dan tidak izinkan duplikat.
thisdict = {"brand": "Ford", "model": "Musta", "year": 1964}
print(thisdict)


# Item dict diurutkan, dapat diubah, dan tidak mengizinkan duplikat.
# Item dict disajikan dalam pasangan key:value, dan dapat dirujuk oleh menggunakan nama kunci.
thisdict = {"brand": "Ford", "model": "Musta", "year": 1964}
print(thisdict["brand"])


# Ordered or Unordered?
# Ketika kita mengatakan bahwa dictionaries are ordered, itu berarti bahwa item memiliki
# urutan yang ditentukan, dan urutan itu tidak akan berubah.
# Unordered berarti barang tidak memiliki urutan yang ditentukan, Anda tidak dapat
# merujuk ke item dengan menggunakan indeks.


# Changeable
# dictionaries dapat diubah, artinya kita dapat mengubah, menambah, atau menghapus item
# setelah kamus telah dibuat.


# Duplikat Tidak Diizinkan
# dictionaries tidak dapat memiliki dua item dengan kunci yang sama:
thisdict = {"brand": "Ford", "model": "Musta", "year": 1964, "year": 2020}
print(thisdict)


# Panjang dictionaries
# Untuk menentukan berapa banyak item yang dimiliki kamus, gunakan fungsi: len()
thisdict = {"brand": "Ford", "model": "Musta", "year": 1964}
print(len(thisdict))


# Item dictionaries - Jenis Data
# Nilai dalam item kamus dapat berupa tipe data apa pun:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
print(thisdict)


# type()
# Dari sudut pandang Python, kamus didefinisikan sebagai objek dengan tipe data 'dict':
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(type(thisdict))


# The dict() Konstruktor
# Dimungkinkan juga untuk menggunakan dikt() konstruktor untuk membuat kamus.
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)
