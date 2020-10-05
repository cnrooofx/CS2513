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

printTriangle(6)
