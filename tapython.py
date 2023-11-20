import module_

print("pilih bangun ruang yang akan di hitung?")
print("1.lingkaran")
print("2.segitiga")
print("-"*40)

a =int(input("ketik pilih: "))

if a == 1:
    module_.lingkaran()
elif a == 2:
    print("hitung segitiga")
    alas = int(input("masukan nilai alas : "))
    tinggi = int(input("masukan nilai tinggi : "))
    sisi = int(input("masukan sisinya : "))
    module_.segitiga(alas,tinggi,sisi)
