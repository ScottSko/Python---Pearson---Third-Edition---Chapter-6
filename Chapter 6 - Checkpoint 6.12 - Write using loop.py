def main():

    my_file = open("checkpoint.txt", 'w')

    for x in range(0, 10):

        my_file.write(str(x + 1) + '\n')

    my_file.close()

main()