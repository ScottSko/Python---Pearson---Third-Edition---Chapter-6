def main():

    stopper = 0

    search = input("What is the name of the file?")

    num_file = open(search + ".txt", "r")

    while stopper != 5:

        line = num_file.readline()

        print(line)

        stopper += 1

    #for line in num_file:
    #    print(line)
    #    stopper += 1

#        if stopper == 5:
#            break

    num_file.close()

main()