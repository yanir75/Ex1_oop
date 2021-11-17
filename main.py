import Json
import numpy as np


def main():
    buildings = ["B1.json", "B2.json", "B3.json", "B4.json", "B5.json"]
    calls_cases = ["calls_a.csv", "calls_b.csv", "calls_c.csv", "calls_d.csv"]
    ind = 1
    for i in buildings:
        ch = chr(97)
        ind1 = 1
        for j in calls_cases:
            st = f'{ind}{ch}'
            Json.read_calculate_write(i, j, st)
            ch = chr(97 + ind1)
            ind1 += 1
        ind += 1
    # Json.read_calculate_write(buildings[4], calls_cases[3], "00")


if __name__ == "__main__":
    main()