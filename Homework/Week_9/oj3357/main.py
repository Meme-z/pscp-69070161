"""www"""
def main():
    """www"""
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    c = 0
    for i, v in enumerate(a):
        if (i == 0 or v > a[i - 1]) and (i == n - 1 or v > a[i + 1]):
            c += 1
    print(c)
main()
