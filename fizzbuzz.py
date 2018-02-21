#fizz-Buzz Using if

# for num in range (1,100):
#     string = ""
#     if num % 3 == 0:
#         string = string + "fizz"
#     if num % 5 == 0:
#         string = string + "buzz"
#     if num % 5 !=0 and num % 3 !=0:
#         string = string + str(num)
#     print(string)
#
# for num in range (1,100):
#     if num % 3 == 0 and num %5 == 0:
#         print("Fizz-Buzz")
#
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)

def fizzbuzz():
    count = input("Enter Value :")
    count = int(count)
    for num in range (1,count):
        if num % 3 == 0 and num %5 == 0:
            print("Fizz-Buzz")

        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
fizzbuzz()
