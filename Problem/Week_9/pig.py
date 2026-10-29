"""pig"""
def main():
    """wow"""
    big = []
    duo = int(input())
    num = input().split()
    if duo == 1:
        print(max(num))
    else:
        for i in range(duo):
            if int(num[2*i+1]) > int(num[2*i]):
                big.append(int(num[2*i+1]))
            elif int(num[2*i+1]) < int(num[2*i]):
                big.append(int(num[2*i]))
            elif int(num[2*i+1]) == int(num[2*i]):
                big.append(int(num[2*i]))
        print(f"{ ' + '.join(str(i) for i in big) } = { sum(big) }")
main()
