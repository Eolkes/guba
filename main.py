#   1
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

num = int(input("Введите число: "))
if isPrime(num):
    print(f"{num} - простое число")

else:
    print(f"{num} - не простое число")


#   2

arr = [5, 2, 9, 3, 8, 6]
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(arr)
print(f"Отсортированный массив: {arr}")


#   3
arr = [5, 2, 9, 3, 8, 6]
def findMax(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

res = findMax(arr)
print(f"Наибольший элемент в массиве: {res}")


#   4
num = int(input("Введите номер числа Фибоначчи: "))
def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

    else:
        return n

res = fibonacci(num)
print(f"Число Фибоначчи под номером {num} равно {res}")


#   5
str = ["apple", "banana", "apple", "cherry", "banana"]
def mostCommonString(strings):
    counts = {}
    mostCommon = ""
    maxCount = 0

    for string in strings:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1

        if counts[string] > maxCount:
            maxCount = counts[string]
            mostCommon = string

    return mostCommon

res = mostCommonString(str)
print(f"Наиболее часто встречающаяся строка: {res}")