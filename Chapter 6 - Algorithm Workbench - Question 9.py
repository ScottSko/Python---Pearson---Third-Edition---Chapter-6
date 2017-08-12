def main():

    try:
        x = float("abc123")
        print(x)
    except IOError:
        print("This code caused an IOError")
    except ValueError:
        print("This code caused a ValueError")

    print("The End.")

main()