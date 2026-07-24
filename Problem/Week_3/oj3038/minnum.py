"""main"""
def main():
    """what"""
    low = int(input())
    for _ in range(2):
        num = int(input())
        if num < low:
            low = num
    print(low)
main()
