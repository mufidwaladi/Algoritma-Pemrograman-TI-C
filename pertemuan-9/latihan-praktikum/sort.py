#INSERTION SORT
def insert_sort(array):
  n = len(array)
  for i in range(1,n):
    insert_index = i
    current_value = array.pop(i)
    for j in range(i-1, -1, -1):
      if array[j] > current_value:
        insert_index = j
    array.insert(insert_index, current_value)
  return array



#QUICK SORT

def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
      high = len(array) - 1
  if low < high:
      pivot_index = partition(array, low, high)
      quicksort(array, low, pivot_index-1)
      quicksort(array, pivot_index+1, high)
      return array



#COUNTING SORT
def counting_sort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

def main():
  panjang = int(input("Masukkan jumlah elemen yang ingin digunakan : "))
  array = []
  for _ in range(panjang):
    angka = int(input("Masukkan angka array : "))
    if angka >= 0:
      array.append(angka)
    else:
      print("Masukkan angka bilangan bulat non negatif !")
  
  print("Sebelum diurutkan:", array)
  insert = insert_sort(array.copy())
  quick = quicksort(array)
  count = counting_sort(array.copy())
  
  
  print(insert)
  print(count)
  print(quick)
  
  


if __name__ == "__main__":
    main()

