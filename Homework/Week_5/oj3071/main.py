"""main"""
def main():
    """abdr"""
    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())
    many = 0
    for x in range(A,B+1):
        if x % d == r:
            many += 1
    print(many)
main()
