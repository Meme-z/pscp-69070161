"""wow"""
def main():
    """wow"""
    km = int(input())
    price = 0
    if km == 1:
        price = 35
    elif 1 < km <= 10:
        price = (km-1)*5+35
    elif km > 10:
        price = 80 + (km-10)*8
    print(price)
main()
