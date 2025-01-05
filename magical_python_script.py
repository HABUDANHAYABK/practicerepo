# This python file is magical, its diplays FIZZBUZZ when a input is divisible by 3 and 5
#it returns FIZZ when the input is only divisible by 3 and BUZZ when the input is only  divisible by 5

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FIZZBUZZ"
    if input % 3 == 0:
        return "FIZZ"
    if input % 5 == 0:
        return "BUZZ"
    return input
print(fizz_buzz(6))
print(fizz_buzz(15))