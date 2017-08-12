def main():

    name = open("my_name.txt", 'w')

    your_name = input("What is your name? ")

    name.write(your_name + "\n")

    name.close()

main()