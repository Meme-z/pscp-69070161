"""expo"""
def main():
    """func"""
    go = input()
    x = 0
    y =0
    for t in go:
        if t == "N":
            y += 1
        elif t == "S":
            y -= 1
        if t == "E":
            x += 1
        elif t == "W":
            x -= 1
    print(f"{x} {y} {abs(x)+abs(y)}")
main()
