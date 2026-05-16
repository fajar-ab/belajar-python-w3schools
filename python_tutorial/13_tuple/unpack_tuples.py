# Saat kita membuat tupel, biasanya kita memberikan nilai padanya.
# Ini disebut "packing" tupel:

fruits = ("apple", "banana", "cherry")
print(fruits)

# Namun, dengan Python, kita juga diperbolehkan mengekstrak nilai 
# kembali ke dalam variabel. Ini disebut "unpacking"
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Jumlah variabel harus sesuai dengan jumlah nilai dalam tupel, 
# jika tidak, Anda harus menggunakan tanda bintang untuk 
# mengumpulkan nilai yang tersisa sebagai list.
fruits = ("apple", "banana", "cherry", "stawberry", "rasberry")
green, yellow, *red = fruits

print(green)
print(yellow)
print(red)