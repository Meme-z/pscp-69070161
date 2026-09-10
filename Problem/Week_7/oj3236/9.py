"""xd"""
def main():
    """w7"""
    long = int(input())
    p1 = input()
    p2 = input()
    count = 0
    for i in range(long):
        if int(p1[i]) + int(p2[i]) != 9:
            count += 1
    if not count:
        print("YES")
    else:
        print(f"NO {count}")
main()
