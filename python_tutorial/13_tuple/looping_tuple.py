# Anda dapat mengulang item tupel dengan menggunakan a for loop
thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)


# dapat mengulang item tupel dengan mengacu pada nomor indeksnya.
# Gunakan range() and len() berfungsi untuk membuat iterable yang sesuai.
thistuple = ("apple", "banana", "cherry")

for i in range(len(thistuple)):
    print(thistuple[i])


# dapat mengulang item tupel dengan menggunakan a while loop.
thistuple = ("apple", "banana", "cherry")

index = 0
while index < len(thistuple):
    print(thistuple[index])
    index += 1


