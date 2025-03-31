with (open("Langdat/prog213b.txt", 'r') as f):
    for line in f:
        num = int(f.readline())
        cost = 0.00
        if 99 >= num >= 0:
            cost = 5.95
        elif 199 >= num >= 100:
            cost = 5.75
        elif 299 >= num >= 200:
            cost = 5.40
        elif 300 >= num:
            cost = 5.15
        num = int(f.readline())
        print("Amount: ", num)
        print("Price: ", cost)
        print("Amount Due: ", cost*num)
        print("")


