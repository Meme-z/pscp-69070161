"""xd"""
def main():
    """w7"""
    info = input().split()
    size = int(info[0])
    k = ord(info[1])
    for i in range(size):
        if k == 35:
            char = "#"
        else:
            char = chr(k + abs(size // 2 - i))
        for j in range(size):
            if i == j or i + j == size - 1:
                print(char, end="")
            else:
                print("-", end="")
        print()
main()
