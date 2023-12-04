def main():
    with open("input.txt") as f:
        copies = dict(zip([i for i in range(1, 209)], [1 for i in range(1, 209)]))

        for index, line in enumerate(f.readlines()):
            splittedLine = line.strip().split("|")

            luckyNumbers = [i for i in splittedLine[0].split(": ")[1].split(" ") if i]
            chosenNumbers = [i for i in splittedLine[1].split(" ") if i]

            winningsNumbers = set(luckyNumbers).intersection(chosenNumbers)
            if winningsNumbers:
                for i in range(index + 2, index + 2 + len(winningsNumbers)):
                    copies[i] = copies[i] + copies[index + 1]

        print(sum(copies.values()))


if __name__ == "__main__":
    main()
