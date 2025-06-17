    
'''
     modulo operator
     10 % 5 = 0 (no remainder in division)
     if 10 % 3 means:
     10 / 3 = 1
     hence, 10 % 3 = 1

'''

print("Welcome to Odd or Even checker!")

number = int(input("What is the number do you want to check? "))

if number % 2 == 0:
    print("It is an even number!")

else:
    print("It is an odd number!")