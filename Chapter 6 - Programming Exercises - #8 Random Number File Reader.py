def main():

    total = 0

    steps = 0

    test_file = open("random.txt", 'r')

    for line in test_file:

        line = int(line)

        total += line

        steps += 1

    print("The sum of all the numbers in the file is", total)
    print("There are", steps, "total numbers in the file.")

main()