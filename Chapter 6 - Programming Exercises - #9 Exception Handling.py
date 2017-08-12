def main():

    try:
        total = 0

        steps = 0

        test_file = open("numbers.txt", 'r')

        for line in test_file:

            line = int(line)

            total += line

            steps += 1

        print(total / steps)

    except IOError:
            print("There was an IOError")
    except ValueError:
            print("There was a ValueError")

main()