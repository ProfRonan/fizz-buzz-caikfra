number = input('Digite umm número: ')
number = int(number)

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz') 
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)