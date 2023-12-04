def main():
    with open("input.txt") as f:
        sum = 0

        for line in f.readlines():
            splittedLine = line.strip().split("|")

            luckyNumbers = [i for i in splittedLine[0].split(": ")[1].split(" ") if i]
            chosenNumbers = [i for i in splittedLine[1].split(" ") if i]

            winningsNumbers = set(luckyNumbers).intersection(chosenNumbers)
            if winningsNumbers:
                sum += 1 * 2**(len(winningsNumbers) - 1)

        print(sum)


if __name__ == "__main__":
    main()
