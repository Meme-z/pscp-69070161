"""www"""
def main():
    """www"""
    m = int(input())
    n = int(input())
    s1 = set()
    for _ in range(m):
        s1.add(int(input()))
    s2 = set()
    for _ in range(n):
        s2.add(int(input()))
    com = s1.intersection(s2)
    if not com:
        print("Nope")
    else:
        for x in sorted(com, reverse=True):
            print(x)
main()
