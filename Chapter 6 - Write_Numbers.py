def main():

    myfile = open("numbers.txt", 'w')

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter another number: "))

    myfile.write(str(num1) + '\n')
    myfile.write(str(num2) + '\n')
    myfile.write(str(num3) + '\n')

    total = num1 + num2 + num3

    myfile.close()
    print("The total for the three numbers is ", total, ".", sep='')
    print("That much has been data written to numbers.txt")

main()