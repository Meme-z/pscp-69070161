"""www"""
def main():
    """www"""
    num = []
    while True:
        line = input()
        if not line:
            continue
        if line == "-1":
            break
        num.append(int(line))
    r = []
    for n in num:
        if r and n == r[-1][1] + 1:
            r[-1][1] = n
        else:
            r.append([n, n])
    print(", ".join(str(g) if g == s else f"{g}-{s}" for g, s in r))
main()
