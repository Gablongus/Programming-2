def main():
    try:
        with open("FILENAME", 'r') as f:
            ... #TODO: replace; (for line in f: or lines = f.readlines())
    except IOError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()