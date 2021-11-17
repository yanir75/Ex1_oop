import Json
import numpy as np


def main():
    buildings = ["B1.json", "B2.json", "B3.json", "B4.json", "B5.json"]
    calls_cases = ["calls_a.csv", "calls_b.csv", "calls_c.csv", "calls_d.csv"]
    # ind1 = np.arange(1, 6)
    # ind2 = ["a", "b", "c", "d"]
    # i = j = 0
    # for b in buildings:
    #     curr_ind1 = ind1[i]
    #     for c in calls_cases:
    #         curr_ind2 = ind2[j]
    #         symbol = str(curr_ind1) + str(curr_ind2)
    #         Json.read_calculate_write(b, c, symbol)
    #         j += 1
    #     i += 1
    Json.read_calculate_write(buildings[2], calls_cases[2], "3c")


if __name__ == "__main__":
    main()