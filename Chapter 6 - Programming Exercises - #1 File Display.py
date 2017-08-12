def main():

    num_file = open("numbers.txt", 'r')

    for line in num_file:

        print(line)

    num_file.close()

main()