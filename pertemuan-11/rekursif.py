def RecSum(arr, n):
    if n <= 0:
        return 0 #Bagian sini yang mengembalikan nilai hasil penjumlahannya
    return RecSum(arr, n - 1) + arr[n - 1]


def arraysum(arr):
    return RecSum(arr, len(arr))

# Driver code
arr = [1, 2, 3, 4, 5]
print(arraysum(arr))

def TowerOfHanoi(n, fromRod, toRod, auxRod):
    if n == 0:
        return
    TowerOfHanoi(n - 1, fromRod, auxRod, toRod)
    print("Disk ", n ," moved from ", fromRod, " to ", toRod)
    TowerOfHanoi(n - 1,auxRod, toRod, fromRod)
if __name__ == "__main__":
    n = 3
    
    # A, C, B are the name of rods
    TowerOfHanoi(n, 'A', 'C', 'B')
