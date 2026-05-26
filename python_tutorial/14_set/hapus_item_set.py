# Untuk menghapus item dalam satu set, gunakan remove(), atau the discard() method

# Hapus "banana" dengan menggunakan remove() method
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
# thisset.remove("kiwi") # Jika item yang akan dihapus tidak ada, remove() akan menimbulkan kesalahan

print(thisset)


# Hapus "banana" dengan menggunakan discard() method
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
thisset.discard("kiwi") # Jika item yang akan dihapus tidak ada, discard() akan TIDAK menimbulkan kesalahan

print(thisset)


# Hapus item acak dengan menggunakan pop() method
thisset = {"apple", "banana", "cherry"}

# Nilai kembalian dari pop() metode adalah item dihapus
x  = thisset.pop()

print(x)


# clear() metode mengosongkan himpunan
thisset = {"apple", "banana", "cherry"}

thisset.clear()
print(thisset)


# del keyword akan menghapus set sepenuhnya:
thisset = {"apple", "banana", "cherry"}

try:
    del thisset
    print(thisset)

except NameError as e:
    print(e)
    