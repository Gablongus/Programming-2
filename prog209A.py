def main():
    try:
        with open("Langdat/prog215a.dat", 'r') as f:
            more = 0
            less = 0
            total = 0

            for line in f:
                data = line.split(" ")
                for i in data:
                    if int(data[0]) >= 500:
                        more += 1
                    elif int(data[0]) < 500:
                        less += 1
                    total += 1

            print("More than or equal to 500: " + str(more))
            print("Less than 500: " + str(less))
            print("Total numbers: " + str(total))


                # Option 2: List Comprehension
                # id, code, sales = [float(x) for x in line.split(" ")]
                # Option 3: Conditional List Comprehension
                # id, code, sales = [float(x) if '.' in x else int(x) for x in line.split(" ")]
    except Exception as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()