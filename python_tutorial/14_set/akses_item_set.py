# tidak dapat mengakses item dalam satu set dengan mengacu pada indeks atau kunci
thisset = {"apple", "banana", "cherry"}

for item in thisset:
    print(item)

# Periksa apakah "banana" ada di set:
print("banana" in thisset)

# Periksa apakah "banana" tidak ada di set:
print("banana" not in thisset)

# Setelah satu set dibuat, tidak dapat mengubah itemnya, tetapi dapat menambahkan item baru