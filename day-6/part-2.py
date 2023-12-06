def main():
    with open("input.txt") as f:

        lines = f.readlines()
        times = [i for i in lines[0].rstrip().split(":")[1].split(" ") if i]
        distances = [i for i in lines[1].rstrip().split(":")[1].split(" ") if i]

        time = int("".join(str(element) for element in times))
        distance = int("".join(str(element) for element in distances))

        waysToWin = 0
        for possibleTime in range(1, time):
            possibleDistance = (time - possibleTime) * possibleTime
            if possibleDistance > distance:
                waysToWin += 1

        print(waysToWin)

if __name__ == "__main__":
    main()
