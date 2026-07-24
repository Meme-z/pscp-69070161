"""main"""
def main():
    """what"""
    loop = int(input())
    low = int(input())
    for _ in range(loop-1):
        num = int(input())
        if num < low:
            low = num
    print(low)
main()
