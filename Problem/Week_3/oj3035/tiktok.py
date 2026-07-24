"""main"""
def main():
    """what"""
    unit = input().split()
    r = int(unit[0])
    x = int(unit[1])
    y = int(unit[2])
    if x**2 + y**2 == r**2:
        print("ON")
    elif x**2 + y**2 < r**2:
        print("IN")
    elif x**2 + y**2 > r**2:
        print("OUT")
main()
