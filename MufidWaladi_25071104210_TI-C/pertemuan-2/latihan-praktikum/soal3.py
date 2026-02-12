digit = 0
def jumlah_digit(n):
    total = 0
    while (n > 0):
        digit = n % 10;    
        total += digit;        
        n = n / 10;   
        n = int(n)
    print(total)
    
n = 1234
jumlah_digit(n)