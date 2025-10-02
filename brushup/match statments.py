# match statements

field_role = input('enter your jersey number: ')


match field_role:
    case '1':
        print('you are a goalkeeper')

    case '2':
        print('you are a golee')
    case _:
        print('you are a fan')
