# Operator terner memungkinkan Anda untuk menetapkan satu nilai 
# jika suatu kondisi benar, dan yang lain jika salah
num = 6 

x = "WEEKEN!" if num > 5 else "Workday"

print(x)

# Operator terner dapat digunakan sebagai pengganti elif dalam pernyataan if yang lebih panjang
num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)