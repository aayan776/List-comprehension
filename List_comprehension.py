try:
    input1 = int(input("Enter first number (total 9): "))
    input2 = int(input("Enter second number (total 9): "))
    input3 = int(input("Enter third number (total 9): "))
    input4 = int(input("Enter fourth number (total 9): "))
    input5 = int(input("Enter fifth number (total 9): "))
    input6 = int(input("Enter sixth number (total 9): "))
    input7 = int(input("Enter seventh number (total 9): "))
    input8 = int(input("Enter eighth number (total 9): "))
    input9 = int(input("Enter ninth number (total 9): "))
    list1 = [input1, input2, input3, input4, input5, input6, input7, input8, input9]
    list2 = [x for x in list1 if x % 2 == 0]
    list3 = [y for y in list1 if y % 2 == 1]
    print(f"All even numbers: {list2}")
    print(f"All odd numbers: {list3}")
except ValueError:
    print("Invalid input.")