def main():

    x = 1

    search = input("What is the name of your file?")

    test_file = open(search + ".txt", 'r')

    for line in test_file:

        print(x, ".", sep='',end='')
        print("",line)

        x += 1

main()