def main():

    new_file = open("number_list.txt", "w")

    for x in range(0, 100):

        new_file.write(str(x + 1) + "\n")

    new_file.close()

main()