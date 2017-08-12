def main():

    my_file = open("checkpoint.txt", 'r')

    new_line = my_file.readline()

    while new_line != '':

        line1 = new_line.rstrip("\n")

        print(line1)

        new_line = my_file.readline()

    my_file.close()

main()