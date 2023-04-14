i=0
n=int (input("masukkan batas:"))

for i in range(n):
    if i%2==0:
        print("bilangan:",i)
    i=i+1

#latihan
print("Latihan")
n = int(input("Masukkan nilai n: "))

# Mencari kelipatan bilangan genap dari 0 hingga n
count = 0
for i in range(n+1):
    if i % 2 == 0:
        count += 1

# Menampilkan kelipatan bilangan genap dan jumlah
print("Kelipatan bilangan genap dari 0 hingga", n, "adalah:")
for i in range(0, (count * 2) + 1, 2):
    print(i, end=" ")
print("(", count, "bilangan)")
