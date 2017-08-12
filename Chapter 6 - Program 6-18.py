import os

def main():

    found = False

    search = input("Enter a description to search for: ")
    #new_qty = int(input("Enter the new quantity: "))

    friend_file = open("friends.txt", 'r')

    temp_file = open("temp.txt", 'w')

    descr = friend_file.readline()

    while descr != '':

        #qty = float(friend_file.readline())

        descr = descr.rstrip('\n')

        if descr == search:

            new_descr = input("What would you like the new name to be? ")

            temp_file.write(new_descr + '\n')
            #temp_file.write(str(new_qty + '\n'))

            found = True

        else:

            temp_file.write(descr + '\n')
            #temp_file.write(str(new_qty + '\n'))

        descr = friend_file.readline()

    friend_file.close()
    temp_file.close()

    os.remove('friends.txt')

    os.rename("temp.txt", 'friends.txt')

    if found:
        print("The file has been updated.")
    else:
        print("That item was not found in the file.")

main()