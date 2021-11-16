import Json


def main():
    buildings = ["B1.json", "B2.json", "B3.json", "B4.json", "B5.json"]
    calls_cases = ["calls_a.csv", "calls_b.csv","calls_c.csv", "calls_d.csv"]
    for b in buildings:
        for c in calls_cases:
            Json.read_calculate_write(b, c)


if __name__ == "__main__":
    main()