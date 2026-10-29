"""a"""
def main():
    """w"""
    bon = ""
    f = 0
    w = 0
    e = 0
    n = int(input())
    for _ in range(n):
        s = list(map(int, input().split()))
        if s[0] > s[3]:
            f += s[0]
        else:
            f += s[3]
        if s[1] > s[4]:
            w += s[1]
        else:
            w += s[4]
        if s[2] > s[5]:
            e += s[2]
        else:
            e += s[5]
    if f > w + e:
        bon = "YES"
    else:
        bon = "NO"
    print(f"Total: {f+w+e}")
    print(f"Fire: {f}")
    print(f"Water: {w}")
    print(f"Earth: {e}")
    print(f"Bonus: {bon}")
main()
