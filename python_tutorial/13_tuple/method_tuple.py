# Mengembalikan jumlah kemunculan nilai tertentu dalam sebuah tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5) # Method ini mengembalikan jumlah berapa kali nilai tertentu muncul dalam tuple
print(x)


# Mencari nilai tertentu dalam tuple dan mengembalikan posisi di mana nilai tersebut ditemukan
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)
print(x)