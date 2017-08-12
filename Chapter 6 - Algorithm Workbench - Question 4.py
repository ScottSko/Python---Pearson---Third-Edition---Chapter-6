def main():

    num_file = open("number_list.txt", "r")

    #contents = num_file.read()
    #alternatively, you can use a for loop

    for line in num_file:

        line = line.rstrip('\n')

        print(line)

main()