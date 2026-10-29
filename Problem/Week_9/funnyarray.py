"""aaaaa"""
def main():
    """www"""
    a = []
    for i in range(3):
        a.append(int(input()))
        print(f"Input number {i+1} stored.")
    while True:
        n = int(input())
        if not n:
            break
        if n == 1:
            print("Original order:",*a)
        elif n == 2:
            print("Descending order:",*sorted(a,reverse=True))
        elif n == 3:
            print("Ascending order:",*sorted(a))
main()
