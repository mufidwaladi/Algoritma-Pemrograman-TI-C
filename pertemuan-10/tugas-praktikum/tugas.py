data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]

def RadixSort(data):
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(data)
    exp = 1

    while maxVal // exp > 0:

        while len(data) > 0:
            val = data.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                data.append(val)

        exp *= 10 

    return data

def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

def LinearSearch(data,target):
    if target not in data:
       print("Tidak ada")
    else:
        for i in range(len(data)):
            if data[i] == target:
                print(f"Indeks dari data yang dicari adalah {i} dan Nilainya adalah {data[i]}")
        

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    print(f"Data sebelum di sort{data}")
    
    RadixSort(data)
    print(f"Data setelah di sort {RadixSort(data)}")
    
    mergeSort(data)
    print(f"Data setelah di sort {mergeSort(data)}")
    
    target = int(input("Masukkan angka yang ingin dicari : "))
    
    LinearSearch(data,target)

    hasil = binarySearch(data, target)

    if hasil != -1:
        print(f"Data ditemukan dengan Indeks: {hasil}, dan Nilainya: {data[hasil]}")
    else:
        print("Data tidak ditemukan.")

if __name__ == "__main__":
   main()