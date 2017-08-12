def main():

    total = 0

    steps = 0

    test_file = open("numbers.txt", 'r')

    for line in test_file:

        line = int(line)

        total += line

        steps += 1

    print(total / steps)

main()