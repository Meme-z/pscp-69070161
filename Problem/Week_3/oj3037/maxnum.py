"""main"""
def main():
    """what"""
    high = int(input())
    for _ in range(2):
        num = int(input())
        if num > high:
            high = num
    print(high)
main()
