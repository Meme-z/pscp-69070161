"""main"""
def main():
    """color"""
    color = input().lower()
    color2 = input().lower()
    if color == color2 and color in ("red", "blue", "yellow"):
        print(color.capitalize())
    elif color == "red" and color2 == "yellow" or color == "yellow" and color2 == "red":
        print("Orange")
    elif color == "red" and color2 == "blue" or color == "blue" and color2 == "red":
        print("Violet")
    elif color == "yellow" and color2 == "blue" or color == "blue" and color2 == "yellow":
        print("Green")
    else:
        print("Error")
main()
