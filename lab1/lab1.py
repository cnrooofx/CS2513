# Script Name: lab1.py
# Author: Conor Fox 119322236

# Q1

def temperature(t=0):
    print('Would you like to convert to Celcius of Fahrenheit?')
    print('Press \'c\' for Celcius or \'f\' for Fahrenheit or any other key to quit.')
    choice = input('Your selection: ')
    if choice == 'c' or choice == 'C':
        print('\n' + str(t) + ' degrees Fahrenheit is:')
        t = ((t - 32) / (9/5))
        print(str(t) + ' degrees Celcius')
    elif choice == 'f' or choice == 'F':
        print('\n' + str(t) + ' degrees Celcius is:')
        t = (t * 9/5 + 32)
        print(str(t) + ' degrees Fahrenheit')

# temperature(122)
# temperature(50)

# Q2

def printTriangle(n):
    if n > 0:
        for i in range(1,n+1):
            if i % 2:
                print('o'*i)
            else:
                print('x'*i)

# printTriangle(6)

# Q3

def numbers():
    print('Enter Three Numbers')
    num1 = input('First number: ')
    num2 = input('Second number: ')
    num3 = input('Third number: ')
    if num1 == num2 == num3:
        print('\nAll Equal')
    else:
        print('\nNot Equal')

# numbers()
