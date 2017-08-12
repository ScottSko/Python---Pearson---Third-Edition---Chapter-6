def main():

    total = 0.0

    try:

        infile = open('sales.txt', "r")

        for x in infile:

            amount = float(x)
            total += amount
            print(x)

        infile.close()

        print(format(total, '.2f'))
    except IOError:
        print("Error")
    except ValueError as err:
        print("Error # 2:\n", err)
    except Exception as error:
        print("Default Error Message")
        print(error)

main()