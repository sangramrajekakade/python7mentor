# lower = int(input("Enter lower Number: "))
# upper = int(input("Enter upper Number: "))
#
# print("Prime numbers between",lower,"and",upper,"are:")
#
# for num in range(lower,upper + 1):
#    # prime numbers are greater than 1
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)



def is_prime_number():
    lower = int(input("Enter lower Number: "))
    upper = int(input("Enter upper Number: "))
    print("Prime numbers between",lower,"and",upper,"are:")

    for num in range(lower,upper +1):

        if num > 1:
            for i in range(2,num):
                if (num % i)==0:
                    break
            else:
                print(num)

is_prime_number()