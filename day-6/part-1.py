def main():
    with open("input.txt") as f:

        multipliedWayToWin = 1

        lines = f.readlines()
        times = [int(i) for i in lines[0].rstrip().split(":")[1].split(" ") if i]
        distances = [int(i) for i in lines[1].rstrip().split(":")[1].split(" ") if i]

        for index in range(0, len(times)):
            waysToWin = 0
            for time in range(1, times[index]):
                distance = (times[index] - time) * time
                if distance > distances[index]:
                    waysToWin += 1

            multipliedWayToWin *= waysToWin

        print(multipliedWayToWin)

if __name__ == "__main__":
    main()
