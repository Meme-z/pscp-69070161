"""xd"""
def main():
    """w7"""
    g = int(input())
    r = int(input())
    if 0 > g or 0 > r or g > 6 or r > 6:
        print("Invalid")
    else:
        if g == r:
            print("Correct!")
        else:
            print("Wrong!")
main()
