# dapat mengulang item list pada list dengan menggunakan for loop
this_list = ["apple", "banana", "cherry"]

for x in this_list:
    print(x)


# juga dapat mengulang item list dengan mengacu pada nomor index mereka
this_list = ["apple", "banana", "cherry"]

for i in range(len(this_list)):
    print(this_list[i])

# juga dapat mengulang item list, menggunakan while loop 
this_list = ["apple", "banana", "cherry"]

i = 0
while i < len(this_list):
    print(this_list[i]) 
    i = i + 1

# list comprehension menawarkan sintaks terpendek untuk 
this_list = ["apple", "banana", "cherry"]
[print(x) for x in this_list]

