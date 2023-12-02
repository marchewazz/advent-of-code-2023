def main():
    with open("input.txt") as f:
        sum = 0

        for line in f:
            minCubes = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            for set in line.strip().split(":")[1].split(";"):
                for cubes in set.split(","):
                    amount = int(cubes.strip().split(" ")[0])
                    color = cubes.strip().split(" ")[1]

                    if amount > minCubes[color]: minCubes[color] = amount

            sum += minCubes["red"]*minCubes["green"]*minCubes["blue"]

        print(sum)
if __name__ == "__main__":
    main()
