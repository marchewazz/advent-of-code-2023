def main():

    def determineMaps(line):
        maps = []

        for i in range(1, len(line)):
            maps.append([*map(int, line[i].split(" "))])

        return maps

    with open("input.txt") as f:
        tempLines = []
        seeds = []
        maps = {
            "seedToSoil": [],
            "soilToFert": [],
            "fertToWater": [],
            "waterToLight": [],
            "lightToTemp": [],
            "tempToHum": [],
            "humToLoc": []
        }

        for line in f:
            if line.rstrip():
                tempLines.append(line.rstrip())
            if not line.strip():
                if "seeds" in tempLines[0]:
                    seeds = [*map(int, tempLines[0].split(": ")[1].split(" "))]
                if "seed-to-soil" in tempLines[0]:
                    maps["seedToSoil"] = determineMaps(tempLines)
                if "soil-to-fertilizer" in tempLines[0]:
                    maps["soilToFert"] = determineMaps(tempLines)
                if "fertilizer-to-water" in tempLines[0]:
                    maps["fertToWater"] = determineMaps(tempLines)
                if "water-to-light" in tempLines[0]:
                    maps["waterToLight"] = determineMaps(tempLines)
                if "light-to-temperature" in tempLines[0]:
                    maps["lightToTemp"] = determineMaps(tempLines)
                if "temperature-to-humidity" in tempLines[0]:
                    maps["tempToHum"] = determineMaps(tempLines)
                if "humidity-to-location" in tempLines[0]:
                    maps["seedToSoil"] = determineMaps(tempLines)

                tempLines = []
        else:
            maps["humToLoc"] = determineMaps(tempLines)

        for index, seed in enumerate(seeds):
            tempValue = seed
            for item in maps.values():
                for row in item:
                    if row[1] <= tempValue < row[1] + row[2]:
                        tempValue = row[0] + (tempValue - row[1])
                        break

            seeds[index] = tempValue
        print(min(seeds))

if __name__ == "__main__":
    main()
