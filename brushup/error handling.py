# Example 1

try:
    number = int(input('enter a number:'))
except ValueError as e:
    print('Thats not a number ')
    print('error:',e)
finally:
    print('Completed')

