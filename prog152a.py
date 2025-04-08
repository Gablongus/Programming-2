import sys
sys.setrecursionlimit(5000)

def add(n):
    if n > 9670: return 0
    return n + add(n+3)

def main():
    print(f"Total = {add(3)}")

if __name__ == '__main__':
    main()

#15586428