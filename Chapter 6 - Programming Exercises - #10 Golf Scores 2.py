def main():

    new_file = open("golf.txt", 'r')

    for line in new_file:

        line = line.rstrip("\n")

        print(line)

    new_file.close()

main()