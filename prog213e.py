def main():
    with (open("Langdat/prog213e.dat", 'r') as f):
        amount = int(f.readline())
        for num in range(0, amount):
            num = int(f.readline())



if __name__ == "__main__":
    main()