def main():

    total = 0

    test_file = open("friends.txt", 'r')

    for line in test_file:

        total += 1

    print(total)

main()