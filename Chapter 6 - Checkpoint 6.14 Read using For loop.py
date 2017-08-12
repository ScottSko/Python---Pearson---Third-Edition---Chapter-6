def main():

    my_file = open("checkpoint.txt", 'r')

    for line in my_file:

        amount = float(line)

        print(format(amount, '.2f'))

    my_file.close()

main()