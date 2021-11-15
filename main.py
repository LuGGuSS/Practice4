# # 1
from copy import copy

arr = []
for i in range(0, 4):
    arr.append(int(input(f"input number {i + 1}: ")))
arr.sort()
arr.reverse()
print(arr[0])

print()

# 2
year = int(input("input year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("366 days")
else:
    print("365 days")

print()

# 3
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a < b+c and b < a+c and c<a+b:
    print("Triangle exists")
else:
    print("Triangle doesn't exist")

print()

# 4
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=" ")

print()

# 5
x = int(input("Factorial : "))
factorial = 1
for i in range(1, x+1):
    factorial *= i

print(f"Factorial of number {x} = {factorial}")

# 6
clock_size = int(input("Input clock size (odd number): "))
if clock_size % 2:
    stars = copy(clock_size)
    while stars >= 1:
        s = "*"*stars
        print(f"{s:^{clock_size}}")
        stars -= 2
    stars = 3
    while stars <= clock_size:
        s = "*" * stars
        print(f"{s:^{clock_size}}")
        stars += 2
else:
    print("You entered even number!")

print()

# 7
for i in range(2, 101):
    half = int(i/2)
    j = 1
    times_devided = 0
    while j <= half and times_devided <= 1:
        if i % j == 0:
            times_devided += 1
        j += 1
    if times_devided <= 1:
        print(i, end=" ")

print()
