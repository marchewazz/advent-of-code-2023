def main():
    with open("input.txt") as f:
        sum = 0

        for line in f:
            firstDigit = None
            lastDigit = None

            for char in line:
                if char.isnumeric():
                    if not firstDigit: firstDigit = int(char)
                    if not lastDigit: lastDigit = int(char)
                    lastDigit = int(char)

            sum += int(f'{firstDigit}{lastDigit}')

        print(sum)

if __name__ == "__main__":
    main()
