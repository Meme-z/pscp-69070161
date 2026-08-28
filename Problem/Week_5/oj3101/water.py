"""wow"""
def main():
    """wow"""
    temp = int(input())
    unit = input().lower()
    if unit == "c":
        if temp <= 0:
            print("solid")
        elif temp < 100:
            print("liquid")
        elif temp >= 100:
            print("gas")
    elif unit == "f":
        if temp <= 32:
            print("solid")
        elif temp < 212:
            print("liquid")
        elif temp >= 212:
            print("gas")
main()
