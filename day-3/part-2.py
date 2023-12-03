def main():
    with open("input.txt") as f:
        ratio = 0
        linesOfFile = f.readlines()

        def calculateNumber(line, startIndex):
            number = line[startIndex]
            for i in range(startIndex - 1, -1, -1):
                if not line[i].isnumeric():
                    break
                else:
                    number = line[i] + number
            for i in range(startIndex + 1, len(line)):
                if not line[i].isnumeric():
                    break
                else:
                    number = number + line[i]
            return int(number)

        for lineIndex, line in enumerate(linesOfFile):
            for charIndex, char in enumerate(line.strip()):
                if not char.isnumeric() and char != ".":
                    numbers = []
                    # IT TURNED OUT TO NO NEED TO CHECK FOR BORDERS
                    if 0 < lineIndex < len(linesOfFile) - 1:
                        if 0 < charIndex < len(line) - 1:
                            if line[charIndex - 1].isnumeric():
                                numbers.append(calculateNumber(line, charIndex - 1))
                            if line[charIndex + 1].isnumeric():
                                numbers.append(calculateNumber(line, charIndex + 1))

                            if linesOfFile[lineIndex - 1][charIndex].isnumeric():
                                numbers.append(calculateNumber(linesOfFile[lineIndex - 1], charIndex))
                            else:
                                if linesOfFile[lineIndex - 1][charIndex] == ".":
                                    if linesOfFile[lineIndex - 1][charIndex - 1].isnumeric():
                                        numbers.append(calculateNumber(linesOfFile[lineIndex - 1], charIndex - 1))
                                    if linesOfFile[lineIndex - 1][charIndex + 1].isnumeric():
                                        numbers.append(calculateNumber(linesOfFile[lineIndex - 1], charIndex + 1))
                                else:
                                    if linesOfFile[lineIndex - 1][charIndex - 1].isnumeric():
                                        numbers.append(calculateNumber(linesOfFile[lineIndex - 1], charIndex - 1))
                                    elif linesOfFile[lineIndex - 1][charIndex + 1].isnumeric():
                                        numbers.append(calculateNumber(linesOfFile[lineIndex - 1], charIndex + 1))

                            if linesOfFile[lineIndex + 1][charIndex].isnumeric():
                                numbers.append(calculateNumber(linesOfFile[lineIndex + 1], charIndex))
                            else:
                                if linesOfFile[lineIndex + 1][charIndex] == ".":
                                    if linesOfFile[lineIndex + 1][charIndex - 1].isnumeric():
                                        numbers.append(calculateNumber(linesOfFile[lineIndex + 1], charIndex - 1))
                                    if linesOfFile[lineIndex + 1][charIndex + 1].isnumeric():
                                        numbers.append(calculateNumber(linesOfFile[lineIndex + 1], charIndex + 1))
                                else:
                                    if linesOfFile[lineIndex + 1][charIndex - 1].isnumeric():
                                        numbers.append(calculateNumber(linesOfFile[lineIndex + 1], charIndex - 1))
                                    elif linesOfFile[lineIndex + 1][charIndex + 1].isnumeric():
                                        numbers.append(calculateNumber(linesOfFile[lineIndex + 1], charIndex + 1))
                    if len(numbers) == 2:
                        ratio += numbers[0] * numbers[1]

        print(ratio)


if __name__ == "__main__":
    main()
