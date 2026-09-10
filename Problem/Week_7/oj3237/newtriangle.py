"""xd"""
def main():
    """w7"""
    size = int(input())
    for i in range(size):
        for j in range(i+1):
            if not j or i == size - 1 or j == i:
                print(0, end="")
            else:
                print(1, end="")
        print()
main()
