def main():

    infile = open("philosophers.txt", "r")

    for x in range(6):
        line1 = infile.readline()

        print(line1)

main()

def method():
    for x in range(5):
        line1 = infile.readline()

        print(line1)

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()

    infile.close()

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)