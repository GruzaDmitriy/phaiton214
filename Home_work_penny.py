n = int(input("Введите колличество копеек: "))
if 0 <= n <= 99:
    print("У вас имеется: ", n, end="")
    if n == 1:
        print(" копейка")
    elif 2 <= n <= 4:
        print(" копейки")
    else:
        print(" копеек")

else:
    print("Слишком много копеек))))")