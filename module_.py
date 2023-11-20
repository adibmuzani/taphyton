import math
def lingkaran():
    a = int(input("masukan nilai r : "))
    print("hitung lingkaran")
    luas = math.pi*a*2
    keliling = 2*math.pi*a
    print(f"luas: {luas}")
    print(f"keliling: {keliling}")
    return luas,keliling 

def segitiga(a,t,s):
    luas = 0.5*a*t
    keliling = s*3
    print("luas: ", luas)
    print("keliling: ", keliling)
    return luas,keliling
    
    

      
        
    
    