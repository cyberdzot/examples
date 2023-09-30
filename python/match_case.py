# Конструкция match-case, аналог switch-case из некоторых других ЯП

value = (5, 2)


match value[1]:
    case 5:
        print('Это цифра 5!')
    case _:
        print('Это другая цифра!')

match value[0]:
    case 5:
        print('Это цифра 5!')
    case _:
        print('Это другая цифра!')

# Это другая цифра!
# Это цифра 5!