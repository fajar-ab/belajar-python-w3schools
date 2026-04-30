# untuk mendapatkan item ke akhir daftar, gunakan method append()
this_list = ["apple", "banana", "cherry"]
this_list.append("orange")

print(this_list)

# untuk memasukkan item list pada index tertentu,gunakan method insert()
this_list = ["apple", "banana", "cherry"]
this_list.insert(1, "orange")

print(this_list)

# untuk menambahkan element dari list lain ke list saat ini, gunakan method extend()
this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

this_list.extend(tropical) # element akan ditambahkan ke end dari list
print(this_list)

# method extend() tidak harus menambah list, dapat menambahkan object iterable apapun
this_list = ["apple", "banana", "cherry"]
this_stuple = ("kiwi", "orange")

this_list.extend(this_stuple)
print(this_list)

