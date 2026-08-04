"""wow"""
import datetime
def main():
    """aa"""
    y1 = int(input())
    m1 = int(input())
    d1 = int(input())
    y2 = int(input())
    m2 = int(input())
    d2 = int(input())
    a = datetime.datetime(y1, m1, d1)
    b = datetime.datetime(y2, m2, d2)
    if abs(a - b).days <= 7:
        print("0")
    elif a >= b:
        print("2")
    elif b >= a:
        print("1")
main()
