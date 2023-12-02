def main():
    with open("input.txt") as f:
        sum = 0

        maxRed = 12
        maxGreen = 13
        maxBlue = 14

        for line in f:
            maxCubes = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            for set in line.strip().split(":")[1].split(";"):
                for cubes in set.split(","):
                    amount = int(cubes.strip().split(" ")[0])
                    color = cubes.strip().split(" ")[1]

                    if amount > maxCubes[color]: maxCubes[color] = amount

            if maxRed >= maxCubes["red"] and maxGreen >= maxCubes["green"] and maxBlue >= maxCubes["blue"]:
                gameID = int(line.strip().split(":")[0].split(" ")[1])
                sum += gameID

        print(sum)
if __name__ == "__main__":
    main()
