import random

def main():

    instances = int(input("How many numbers do you want? "))

    test_file = open("random.txt", 'w')

    for x in range(0, instances):

        random_numbers = random.randint(1, 500)
        test_file.write(str(random_numbers) + "\n")

main()