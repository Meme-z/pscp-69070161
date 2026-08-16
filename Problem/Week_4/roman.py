"""roman"""
def main():
    """wow"""
    num = int(input())
    roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    if 0 < num <= 9:
        print(roman[num-1])
    elif num > 9 or not num:
        print("Error : Out of range")
    elif num < 0:
        print("Error : Please input positive number")
main()
