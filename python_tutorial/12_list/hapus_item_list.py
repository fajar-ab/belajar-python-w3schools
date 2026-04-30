# hapus item yang ditentukan, dengan method remove() 
this_list = ["apple", "banana", "cherry"]

this_list.remove("banana")
print(this_list)

# jika terdapat lebih dari satu item dengan nilai yang ditentukan
# maka method remove() menghapus yang pertama ketemu
this_list = ["apple", "banana", "cherry", "banana", "kiwi"]

this_list.remove("banana")
print(this_list)

# method pop() akam menghapus item yang ditentukan indexnya
this_list = ["apple", "banana", "cherry"]

this_list.pop(1)
print(this_list)

# jika tidak ditentukan indexnya, method akan menghapus item terakhir
this_list = ["apple", "banana", "cherry"]

this_list.pop()
print(this_list)

# keyword `del` juga menghapus yang ditentukan indexnya
this_list = ["apple", "banana", "cherry"]

del this_list[0]
print(this_list)

# keyword `del` juga dapat menghapus list sepenuhnya
this_list = ["apple", "banana", "cherry"]
del this_list

# print(this_list) error karna variabel this_list menjadi tidak terdefinisi

# method clear() akan mengosongkan list, list masih tersisa tapi tidak ada isinya
this_list = ["apple", "banana", "cherry"]

this_list.clear()
print(this_list)

