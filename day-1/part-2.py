def main():
    with open("input.txt") as f:
        sum = 0

        def determineDigit(digit: str) -> int:
            if digit.isnumeric():
                return int(digit)
            else:
                if digit == "zero": return 0
                if digit == "one": return 1
                if digit == "two": return 2
                if digit == "three": return 3
                if digit == "four": return 4
                if digit == "five": return 5
                if digit == "six": return 6
                if digit == "seven": return 7
                if digit == "eight": return 8
                if digit == "nine": return 9

        for line in f:
            digits = {
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": [],
                "7": [],
                "8": [],
                "9": [],
                "0": [],
                "one": [],
                "two": [],
                "three": [],
                "four": [],
                "five": [],
                "six": [],
                "seven": [],
                "eight": [],
                "nine": [],
                "zero": [],
            }

            for digit in digits.keys():
                occurrences = [i for i in range(len(line)) if line.startswith(digit, i)]
                digits[digit] = occurrences

            firstIndex = None
            firstDigit = None
            lastIndex = None
            lastDigit = None

            for digit, occurrences in digits.items():
                if not firstDigit:
                    firstDigit = digit
                    firstIndex = min(occurrences, default=9999999)
                else:
                    if firstIndex > min(occurrences, default=9999999):
                        firstDigit = digit
                        firstIndex = min(occurrences, default=9999999)
                if not lastDigit:
                    lastDigit = digit
                    lastIndex = max(occurrences, default=-1)
                else:
                    if lastIndex < max(occurrences, default=-1):
                        lastDigit = digit
                        lastIndex = max(occurrences, default=-1)

            sum += int(f'{determineDigit(firstDigit)}{determineDigit(lastDigit)}')

        print(sum)

if __name__ == "__main__":
    main()
