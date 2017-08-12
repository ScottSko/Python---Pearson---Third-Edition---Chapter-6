def main():

    tester = "y"

    new_file = open("golf.txt", "w")

    while tester == "y" or tester == "Y":

        name = input("What is the the player's name?")
        score = input("What is the player's score?")

        new_file.write(name + "\n")
        new_file.write(score + '\n')

        tester = input("Would you like to enter another record? (y/n)")

    print("The records were written to the file.")

    new_file.close()

main()