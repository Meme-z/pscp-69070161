"""3027"""
def main():
    """rabbit2"""
    fence = input().split()
    price = int(input())
    width = int(fence[0])
    height = int(fence[1])
    floor = int(fence[2])
    long = (width*2+height*2)*floor
    total = long*price
    print(long)
    print(total)
main()
