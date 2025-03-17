def main():
    try:
        with open("Langdat/prog215a.dat", 'r') as f:
            for line in f:
                data = line.split(" ")
                # TODO: figure this the heck out because you have no idea what you are doing.
                id = int(data[0])
                code = int(data[1])
                sales = float(data[2])

                # Option 2: List Comprehension
                # id, code, sales = [float(x) for x in line.split(" ")]
                # Option 3: Conditional List Comprehension
                # id, code, sales = [float(x) if '.' in x else int(x) for x in line.split(" ")]
    except Exception as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()