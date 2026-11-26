def main():
    # Remove pass with your answer.
    while True:
        try:
            n = int(input("Type an integer: "))
            break
        except ValueError:
            print("Please enter an integer.")

    if n % 10 != 0 or n % 3 == 0:
        print(f"")


if __name__ == "__main__":
    # execute only if run as a script
    main()
