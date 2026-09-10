"""xd"""
def main():
    """w7"""
    info = input().split()
    c = info[0]
    l = int(info[1])
    start = 0
    if c == "R":
        start = 0
    elif c == "G":
        start = 1
    elif c == "B":
        start = 2
    cl = ["Red", "Green", "Blue"]
    for _ in range(l):
        print(cl[start], end=" ")
        start = (start + 1) % 3
main()
