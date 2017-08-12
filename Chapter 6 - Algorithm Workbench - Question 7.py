import os

def main():

    found = False

    search = input("Which student do you want to delete?")

    s_file = open("students.txt", 'r')

    temp_file = open("temp.txt", 'w')

    descr = s_file.readline()

    while descr != '':

        qty = float(s_file.readline())

        descr = descr.rstrip("\n")

        if descr != search:

            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')

        else:

            found = True

        descr = s_file.readline()

    s_file.close()
    temp_file.close()

    os.remove("students.txt")

    os.rename("temp.txt", "students.txt")

    if found:
        print("The file has been updated.")
    else:
        print("That item was not found in the file.")

main()