from operator import truediv

age = 22

if age >= 18:
    message = 'Eligible'
else:
    message = 'Not Eligible'


#Tenary operator

message = 'Eligible' if age >= 18 else 'Not Eligible'


#Logical operators

#('and', 'or', not )

high_income = True
good_credit = True
student = True

#if high_income and good_credit and not student:
    #print('Eligible')

#For Loop


successful = False

for number in range(1,4):
    print('Attempt', number, number * '.')
    if successful:
        print('successful')
        break

else:
    print('Attempted 3 times and failed')


