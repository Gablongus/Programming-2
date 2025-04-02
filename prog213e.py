def main():
    with (open("Langdat/prog213e.dat", 'r') as f):
        less_20 = 0
        less_39 = 0
        less_59 = 0
        less_79 = 0
        more_79 = 0
        amount = int(f.readline())
        for num in range(0, amount):
            age = int(f.readline())
            if age < 20:
                less_20 += 1
            if  39 > age >= 20:
                less_39 += 1
            if  59 > age >= 40:
                less_59 += 1
            if  79 > age >= 60:
                less_79 += 1
            if  age >= 79:
                more_79 += 1
    print("Age Group\tDistribution\tPercentage")
    print("<20\t\t\t", str(less_20), "\t\t\t", round(less_20/17*100, 2))
    print("20 - 39\t\t", str(less_39), "\t\t\t", round(less_39/17*100, 2))
    print("40 - 59\t\t", str(less_59), "\t\t\t", round(less_59 / 17 * 100, 2))
    print("60 - 79\t\t", str(less_79), "\t\t\t", round(less_79 / 17 * 100, 2))
    print(">79\t\t\t", str(more_79), "\t\t\t", round(more_79 / 17 * 100, 2))
if __name__ == "__main__":
    main()