#1) Get an item for user and prompt the option to quit
#2)


shopping_list = []
total = 0
while True:

    #Get item from user
    item = input("Enter item or ('q' to quit):").lower()
    if item == 'q':
       break

    #get price from user & catch the error on invalid value for price

    try:
        price = float(input('enter price:'))
    except ValueError as e:
        print('that is not a valid price')
        continue
    total += price

    shopping_list.append((item, price))
for item, price in shopping_list:
    print(item, price)
print('Toal:',total)
