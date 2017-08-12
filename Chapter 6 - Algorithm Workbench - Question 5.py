def main():

    total = 0

    num_file = open("number_list.txt", "r")

    for line in num_file:

        line = int(line)

        total += line

    print(total)

main()