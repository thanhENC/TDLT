def UCLN(a, b):
    if b == 0:
        return a
    else:
        return UCLN(b, a%b)

def main():
    a, b = [int(num) for num in input().rstrip().split()]
    print(UCLN(a, b))

if __name__ == "__main__":
    main()