"""www"""
def main():
    """www"""
    ing = []
    while True:
        s = input().strip()
        if s == "Cook":
            break
        if s:
            ing.append(s)
    flav = []
    while True:
        s = input().strip()
        if s == "End":
            break
        if s:
            flav.append(s)
    allowed = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
        "Bean Sprouts", "Noodle", "Chives", "Lime",
        "Egg", "Oil", "Peanuts"
    }
    has_invalid = False
    for x in ing:
        if x not in allowed:
            has_invalid = True
            break
    if has_invalid:
        print("This is not Pad Thai!!!")
    elif not allowed.issubset(set(ing)):
        print("This is bad!")
    elif set(flav) == {"Sweet", "Sour", "Salty"}:
        print("Delicious!")
    else:
        print("Not Bad...")
main()
