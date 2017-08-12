def main():

    total = 0

    test_file = open("numbers.txt", 'r')

    for line in test_file:

        line = int(line)

        total += line

    print(total)

main()