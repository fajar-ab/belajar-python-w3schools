# objek list memiliki short() method yang akan 
# mengurutkan list secara alfanumerik, menaik secara default

this_list = ["orange", "mango", "kiwi", "pineaple", "banana"]

this_list.sort()
print(this_list)

# urutkan secara numerik
this_list = [100, 50, 65, 82, 23]

this_list.sort()
print(this_list)

# untuk mengurutkan kenbawah (descending), gunakan argumen keyword reverse = True
this_list = ["orange", "mango", "kiwi", "pineaple", "banana"]

this_list.sort(reverse = True)
print(this_list)

this_list = [100, 50, 65, 82, 23]

this_list.sort(reverse = True)
print(this_list)

# juga dapat menyesuaikan fungsi sendiri dengan mennunakan argumen keyword key = function
# fungsi akan mengembalikan nomor yang akan digunakan untuk list (angka terendah dulu)

# urutkaan list berdasarkan berapa dekat angka tersebut dengan 50
def my_func(n):
    return abs(n - 50)

this_list = [100, 50, 65, 82, 23]
this_list.sort(key = my_func)

print(this_list)

# secara default method sort() adalah case sensitive, mengakibatkan semua huruf kapital
# diurutkan sebelum huruf kecil
this_list = ["banana", "Orage", "Kiwi", "cherry"]

this_list.sort()
print(this_list)

# untungnya dapat menggunakan fungsi built-in sebagai fungsi utama saat mengurutkan list
# jadi jika menginginkan fungsi pengurutan yang tidak peka huruf besar-kecil, gunakan str.lower sebagai fungsi kunci
this_list = ["banana", "Orage", "Kiwi", "cherry"]

this_list.sort(key=str.lower)
print(this_list)

# bagaimana jika ingin membalikkan urutan list, apapun alfabetnya
# method reverse() membalikkan urutan peyortiran elemen saat ini

this_list = ["banana", "Orange", "Kiwi", "cherry"]

this_list.reverse()
print(this_list)