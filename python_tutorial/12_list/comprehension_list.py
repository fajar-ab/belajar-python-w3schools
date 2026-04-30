# menawarkan sintaks yang lebih pendek tetika ingin membuat daftar baru berdasarkan
# nilai pada list yang ada

# tanpa list comperhension dengan for dengan test bersyarat
fruits = ["apple", "banana", "cherry", "kiwi", "manggo"]
new_list = []

for fruit in fruits:
    if "a" in fruit:
        new_list.append(fruit)

print(new_list)

# dengan list comprehendion dapat melakukan semua itu dengan satu baris code
new_list = [fruit for fruit in fruits if "a" in fruit]

print(new_list)

# contoh lain hanya menerima barang yang bukan apple
new_list = [fruit for fruit in fruits if fruit != "apple"]

print(new_list)

# contoh tidak menggunakan if pernyataan
new_list = [fruit for fruit in fruits]

print(new_list)

# iterable apat berupa object apapun yang dapat di ulang
# dapat menggunakan range() fungsi untuk membuat object iterable
new_list = [x for x in range(10)]

print(new_list)

# terima angka yang lebih rendah dari 5
new_list = [x for x in range(10) if x < 5]

print(new_list)

# ekpresi dalah item saat ini dalam iterasi, tapi juga merupakan hasil, yang 
# dapat dimanipulasi sebelum berakhir seperti item list yang baru

# atur list dalam list baru dalam huruf besar
fruits = ["apple", "banana", "cherry"]
new_list = [fruit.upper() for fruit in fruits]

print(new_list)

# atur semua nilai ke 'hallo'
new_list = ['hallo' for x in fruits]

print(new_list)

# ekspesi juga dapat berisi kondisi, tidak seperti filter, tetapi sebagai cara
# utuk memanipulasi hasil
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x if x != "banana" else "orange" for x in fruits]
# kembalikan barangnya jika bukan pisang, jika pisang balikkan jeruk

print(new_list)