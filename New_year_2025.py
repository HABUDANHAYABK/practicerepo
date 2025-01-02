for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} is an even number!")

#check if a number is even or odd
num = int(input("Enter a number "))
if num % 2 == 0:
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')

# List of squares
squares = [i ** 2 for i in range(100)]
print(squares)

# Multiplication table
num = int(input("Enter a number and get its multiplication table"))
for i in range(11):
    product = num * i
    print(f"{num} x {i} =", product)