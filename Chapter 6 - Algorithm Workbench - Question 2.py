def main():

    name = open("my_name.txt", 'r')

    line1 = name.readline()

    print(line1)

    name.close()

main()