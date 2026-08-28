"""wow"""
def main():
    """wow"""
    dest = input()
    kg = float(input())
    price = 0
    if dest == "BKK CNX":
        price = kg*30 + 10
    elif dest == "CNX UBP":
        price = kg*40 + 15
    elif dest == "UBP BKK":
        price = kg*40 + 20
    elif dest == "BKK PKT":
        price = kg*50 + 25
    elif dest == "PKT CNX":
        price = kg*60 + 30
    elif dest == "UBP PKT":
        price = kg*70 + 40
    if not price:
        print("Error")
    else:
        print(f"{price:.2f}")
main()
